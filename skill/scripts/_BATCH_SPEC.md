# Q-SYS 文档批量抓取规范（Batch Spec v1）

> 所有执行 Agent 必须遵守本规范。目标：把 help.qsys.com 官方文档页抓取为结构化 Markdown 知识文件。

## 1. 内容源（已验证可达）

| 分区 | URL 模板 | 说明 |
|------|---------|------|
| Schematic_Library | `https://help.qsys.com/Content/Schematic_Library/<page>.htm` | 组件文档 |
| DeveloperHelp | `https://help.qsys.com/DeveloperHelp/Content/<Section>/<Page>.htm` | 插件开发 |
| Designer | `https://help.qsys.com/Content/Q-SYS_Designer/<page>.htm`（也有 Q-Sys_Designer 大小写） | Designer 软件 |
| Hardware | `https://help.qsys.com/Content/Hardware/<Sub>/<page>.htm` | 硬件 |

⚠️ 不要在 URL 前加 `/q-sys_10.4/`（会 404）。页面直接以静态 HTML 提供，无需浏览器渲染。
⚠️ 已知 404（不要重试）：WebSocket、Dante API、Lua USB HID、dir (Directory)。

## 2. 执行脚本（位于 skill 的 scripts/ 目录）

```
cd /home/user/.doubao/agent_mode/workspace/.user_skills/qsc-qplug-dev/scripts
```

- **批量模式**：`python3 batch_fetch.py <批次.tsv>` — TSV 每行 `url\t输出绝对路径\t显示标题`。成功/失败计数输出到 stdout，失败明细写入同目录 `_batch_failures.log`。
- **单页重试/补抓**：`python3 fetch_qsys_doc.py <url> -o <绝对输出路径> --title "<显示标题>" --source "<来源URL>"`
- 脚本会自动：提取 h1 标题/描述/分区/表格/代码块/Note/Tip、过滤页脚与面包屑、去掉代码行号。
- 若批量执行时某页失败（404/超时/网络），用单页模式重试一次；仍失败则跳过并记录，不要反复重试。

## 3. 输出文件格式（与现有文件一致）

```markdown
# <组件/页面标题>
> 来源: <该页 Content URL>

<首段描述（脚本自动提取）>

## <分区>（如 Properties / Controls / Control Pins / 输入输出引脚）
- 脚本生成的 ### 子项、表格、引用保持不动
- Control Pins 表必须保留为 Markdown 表格（Pin Name | Value | String | Position | Pins Available）

> **Note:** / > **Tip:** 引用保留（即"要点"）
```

**格式参考文件（必须模仿其结构）**：
- `references/q-sys-10.4-docs/Schematic_Library/When.md`、`Flip_Flop.md`（手工精炼风格）
- `references/q-sys-10.4-docs/Schematic_Library/Gain.md`、`Router.md`（本批脚本输出风格，最新基准）

## 4. 抓取后检查（每页都要过一遍）

1. 文件存在且非空；`# 标题` 与 `> 来源:` 行正确。
2. **删除残留垃圾**：页面底部 `Q-SYS Help (Latest Version) | ... | Q-SYS 10.5.0` 页脚、孤立的 `You are here:`、`Open topic with navigation`、`Copy` 按钮字样。
3. **修复表格脚注混入**：若表格末尾混入整段脚注文字（如 `1. Available with Crosspoint buttons only. ...`），把该段移到表格下方成为普通段落。
4. 若出现 `[图片: xxx]` 占位，保留（信息有价值）；若 `[图片: Closed]`/`[图片: Open]` 等折叠图标残留，删除。
5. 代码示例页（DeveloperHelp Code_Examples）必须保留完整代码块（``` 围栏）。
6. 若页面内容为空/全是导航文字（判断为 404 页），删除该输出文件并记录。

## 5. 命名与落盘

- 文件名已在各自批次 TSV 中指定（PascalCase），**不得改名**；输出路径也已在 TSV 中指定。
- 只写你自己的输出目录，**不要修改任何 README.md**（索引由组织者统一更新）。
- 不要删除/覆盖他人文件。

## 6. 完成报告（最终消息必须包含）

- 实际成功抓取数 / 失败数 / 失败明细（URL+原因）
- 生成的完整文件清单（相对路径即可）
