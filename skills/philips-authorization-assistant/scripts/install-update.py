#!/usr/bin/env python3
"""Install an approved update, keeping the previous skill as a backup."""
import argparse
import os
import shutil
import subprocess
import sys
import tempfile
from datetime import datetime
from pathlib import Path

REPO = 'https://github.com/630898288-collab/philips-authorization-assistant.git'
INSTALLED = Path(__file__).resolve().parent.parent

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--yes', action='store_true', help='User has explicitly approved replacing this installation')
    parser.add_argument('--source-skill', help='Local skill source for offline testing')
    parser.add_argument('--install-dir', help='Installation path for offline testing')
    args = parser.parse_args()
    if not args.yes:
        parser.error('Explicit user approval and --yes are required')
    dest = Path(args.install_dir).expanduser().absolute() if args.install_dir else INSTALLED
    if dest.is_symlink() or not dest.is_dir() or not (dest / 'SKILL.md').is_file():
        raise RuntimeError('Expected an existing non-symlink skill directory with SKILL.md')
    with tempfile.TemporaryDirectory(prefix='philips-skill-update-') as tmp:
        if args.source_skill:
            source = Path(args.source_skill).resolve()
        else:
            checkout = Path(tmp) / 'repo'
            subprocess.run(['git', 'clone', '--quiet', '--depth', '1', '--branch', 'main', REPO, str(checkout)], check=True, timeout=60)
            source = checkout / 'skills' / 'philips-authorization-assistant'
        if not (source / 'SKILL.md').is_file() or not (source / 'VERSION').is_file():
            raise RuntimeError('Downloaded source is not a complete skill')
        if any(p.is_symlink() for p in source.rglob('*')):
            raise RuntimeError('Downloaded source contains symlinks')
        stage = Path(tempfile.mkdtemp(prefix='.philips-update-', dir=str(dest.parent)))
        try:
            shutil.copytree(source, stage, dirs_exist_ok=True, ignore=shutil.ignore_patterns('.git', '__pycache__', '*.pyc', '.env', '.env.*'))
            stamp = datetime.now().strftime('%Y%m%d-%H%M%S-%f')
            backup = dest.parent / (dest.name + '.backup-' + stamp)
            os.replace(dest, backup)
            try:
                os.replace(stage, dest)
            except Exception:
                os.replace(backup, dest)
                raise
            print('Updated skill:', dest)
            print('Previous version backup:', backup)
            print('Installed version:', (dest / 'VERSION').read_text(encoding='utf-8').strip())
        finally:
            if stage.exists():
                shutil.rmtree(stage)
    return 0

if __name__ == '__main__':
    try:
        sys.exit(main())
    except (OSError, RuntimeError, subprocess.SubprocessError) as e:
        print('Update failed:', str(e), file=sys.stderr)
        sys.exit(1)
