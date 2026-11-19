# 审核邮件与收件人

收到登记或提交需求时，在需要邮件的流程告诉用户邮件是待完成的必要步骤，并问用户希望**创建草稿**还是在核对后**发送**；用户已明确选择时不要重复问意向。可先准备草稿、核对附件与真实收件地址，再让用户审阅具体收件人/抄送、主题和内容；只有本次对具体内容与收件人的明确发送授权才能使用发送命令。需要邮件但用户没选择时不擅自发送。用户只要求登记不自动发邮件。草稿创建会写入当前用户邮箱，基于用户代办要求或明确选择进行，不以技能创建者身份操作。

## 收件路由

- 独立站：主送 Alex Rishoej，抄送 Gloria Jiang 和各相关区域 MU：MoW Daniel Abbo、NA David Farmer、EU Jakub Grosman。独立站邮件是登记后的额外审批步骤。用户提供的区域负责人更新于 2026-11-19。
- 亚马逊／特殊渠道：A1 规范为主送 Gloria，抄送部门负责人；附登记截图、已签销售合同及平台所需信息。其他渠道按个案确认。
- 海关白名单：A1 为主送 Gloria、抄送部门负责人；培训材料另指定 Jennifer Yan 接收并抄送 Gloria。可同时包含 Jennifer、Gloria 和部门负责人，明确收件/抄送并依据用户及现行要求确认；附登记截图及已签供应商/销售合同。培训要求至少出货前一周提出。
- 国内常规主授权、一级、二级：按规范自行 OA，不臆造一封必须发送的审批邮件；特殊需求/海外个案有邮件要求时由实际负责人或用户确认。

2026-11-19 通讯录定位供消歧，不视为永久有效：Gloria `gloria.jiang@aquashield-ips.com`；Daniel Abbo（MoW）`daniel.abbo@aquashield-ips.com`；David Farmer（北美）`david.farmer@aquashield-ips.com`；Jakub Grosman（欧洲）`jakub.grosman@aquashield-ips.eu`；Jennifer `jennifer.yan@aquashield-ips.com`。Alex 通讯录 email 与 enterprise_email 不同，邮箱收件人搜索显示 `alexrishoej@aquashield-ips.com`；运行时搜索并向用户明确展示候选核实，不把另一个拼写默认为同一地址。对于任何模糊搜索出的收件人，即使仅一个候选，遵循 lark-mail 的收件人确认要求；防止同名者及组织变更。缺少 MU 的明确归属或部门负责人时询问，不自行补全。

## 操作

读取 lark-mail 的 SKILL.md 和当前 `+send --help`、`+draft-send --help`。按用户语言写业务信，包含真实背景、申请编号/记录链接、需要审批的事项和必要材料，不伪造已完成步骤。`lark-cli mail +send --to ... --cc ... --subject ... --body-file ./... --as user` 默认创建草稿；路径相对于当前工作目录。需要附真实截图或合同使用 `--attach ./...`；如果不能取得实际截图，不能附合成图并假装截图，向用户说明并继续可完成部分。草稿创建后核对收件人、内容、附件并给草稿链接（如返回）。直接发送须用户对具体收件人与内容明确确认后，按 lark-mail 流程发送，随后核查投递状态；发送失败时不要重复创建或重复发送，先查询状态。没找到邮箱/权限不足，停在草稿或告诉用户缺什么，不编造地址。
