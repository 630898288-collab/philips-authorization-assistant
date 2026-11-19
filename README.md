# 飞利浦授权与独立站助手

帮助申请人判断品牌授权路径、登记飞书多维表、查询商标证书和独立站进度，并准备审核邮件。AI 不替申请人办理 OA；发送邮件前需得到申请人对收件人和内容的明确同意。

## 安装

在支持 Skill 安装的 AI 助手中发送：

> 请从 https://github.com/630898288-collab/philips-authorization-assistant 安装 `skills/philips-authorization-assistant`，安装后告诉我如何使用。

Codex 用户也可使用自己的 Skill 安装器安装仓库中 `skills/philips-authorization-assistant`。重启或新开会话以确保加载。需要用户自己的飞书账号、目标文档和邮箱权限、`lark-cli` 及相应飞书工具能力；不得共享凭据。不同客户端的安装步骤和可用工具可能不同。

## 更新

每次使用技能时检查 GitHub 的 `VERSION`；网络不可用时继续使用本地版本。发现新版本时会询问使用者，只有同意后才更新，并备份旧版。维护者修改流程、脚本或规则时须递增 `skills/philips-authorization-assistant/VERSION` 再发布。

## 重要边界

- 截图依赖用户已登录的飞书界面和当前 AI 客户端的截图功能；无法获取时返回记录链接和手动截图指引，不伪造系统截图。
- 申请登记、审核邮件和审批结果是不同步骤；以当前受控规范、飞书字段和负责人意见为准。
- 本仓库公开，文内飞书资源仍受各自访问权限限制。
