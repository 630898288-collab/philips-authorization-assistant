#!/usr/bin/env python3
"""Check the published skill version without changing installed files."""
import argparse
import json
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

SKILL = Path(__file__).resolve().parent.parent
URL = 'https://raw.githubusercontent.com/630898288-collab/philips-authorization-assistant/main/skills/philips-authorization-assistant/VERSION'

def parse_version(text):
    version = text.strip()
    if not re.fullmatch(r'\d+\.\d+\.\d+', version):
        raise ValueError('Invalid version format')
    return tuple(int(x) for x in version.split('.'))

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--remote-version', help='Offline version override for validation; not used in normal operation')
    args = ap.parse_args()
    try:
        current = (SKILL / 'VERSION').read_text(encoding='utf-8').strip()
        installed = parse_version(current)
    except (OSError, ValueError) as exc:
        print(json.dumps({'checked': False, 'reason': 'local_version_unavailable', 'detail': str(exc)}))
        return 0
    try:
        if args.remote_version is not None:
            latest = args.remote_version.strip()
        else:
            req = urllib.request.Request(URL, headers={'User-Agent': 'philips-authorization-assistant-update-check'})
            with urllib.request.urlopen(req, timeout=5) as response:
                latest = response.read(64).decode('utf-8').strip()
        remote = parse_version(latest)
    except (OSError, ValueError, UnicodeError, urllib.error.URLError) as exc:
        print(json.dumps({'checked': False, 'current': current, 'reason': 'update_check_unavailable'}))
        return 0
    print(json.dumps({'checked': True, 'current': current, 'latest': latest, 'update_available': remote > installed, 'repository': 'https://github.com/630898288-collab/philips-authorization-assistant'}, ensure_ascii=False))
    return 0

if __name__ == '__main__':
    sys.exit(main())
