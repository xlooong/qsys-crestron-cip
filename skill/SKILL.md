---
name: qsc-qplug-dev
description: "Q-SYS qplug 插件开发技能。当用户要求创建、编辑、调试 Q-SYS Designer 插件（.qplug 文件），或涉及 wxl_personal_plug 系列插件时使用。覆盖控件定义、面板布局、属性参数、运行时 Lua 逻辑、GitHub 发布。Use when creating, editing, or debugging Q-SYS Designer plugins (.qplug), or working with the wxl_personal_plug plugin series."
---

# Q-SYS Qplug Development

## Overview

Q-SYS qplug 是 Q-SYS Designer 的 Lua 插件，单文件包含元信息、属性、控件、布局和运行时逻辑。本技能提供编写规范、控件类型参考、常见陷阱和调试经验。

## 快速参考 / Quick Reference

**编写规范与控件类型**: 读取 `references/qplug-standards.md`
- 9 文件 Plugin Compiler 框架结构
- 必需函数（GetControls/GetProperties/GetControlLayout/GetPages 等）
- Button/Knob/Text/Indicator 控件类型与引脚规则
- 布局图形类型与坐标规范
- 实践验证的常见陷阱表

**DeveloperHelp 官方文档知识库**: 读取 `references/developer-help/README.md`
- Getting_Started/ - Core OS 环境、Script vs Plugin、Building a Plugin
- Standards_Definitions/ - Style Guide、Reserved Control Names、Reserved Functions（27页完整）
- Development_Tools/ - Plugin Compiler、Plugin Encryption Tool
- Code_Examples/ - Basic Framework、Dynamic Pages、Hex Data、TCP/UDP/Serial/SSH/HTTP/JSON/XML/Telnet
- Recommended_Practices/ - TCP/UDP/Serial 最佳实践、Lua Scopes、Pcall、Plugin Debug
- Community/ - Locimation/GitHub/QSC官方社区项目学习笔记

**Schematic 组件库参考（开发最常用）**: 读取 `references/q-sys-10.4-docs/Schematic_Library/`（62 页完整，README 内有清单）
- 脚本组件: Control_Script / Text_Controller / Block_Controller
- 控制组件: Command_Buttons / Custom_Controls / Control_Router / Control_Delay / When / Selector / Sequencer / Flip_Flop / Value_Stepper / Press_and_Hold / Date_Time / Event_Log / LFO / PIN_Pad / Call_Sync / USB_Router / UCI 控制器等
- 音频组件: Gain / Gain_Ramp / Delay / Crossover / Crossfader / Room_Combiner / Router / System_Mute / Audio_File_Recorder / AEC / VAD
- 视频组件: AV_Stream_Router / Camera_Router / Mediacast_Router / NVM_Proxy / VisionSuite
- 布局组件: Channel_Group / Container / Popup_Button / Signal_Snakes
- 每个文件含组件说明/输入输出引脚/属性/Controls/Control Pins 表/Note-Tip 要点

**Designer 软件参考**: 读取 `references/q-sys-10.4-docs/Designer/`（19 页）
- 安装/上手/Emulate 模式/原理图使用/连接布线/图形工具/快捷键/属性面板/查找替换

**CSS/UCI 样式开发**: 读取 `references/css-uci/`
- `CSS_Class_Reference.md` — Q-SYS CSS 类名参考（buttonprimary/buttonsecondary/icons/text类/justify类）
- `UCI_Styles.md` — UCI 样式系统完整指南（filmstrip/layer渲染、动态CSS类、按钮pressed选择器、CSS变量、@import）

**Hardware 硬件参考**: 读取 `references/q-sys-10.4-docs/Hardware/`
- `Processing/Core_Processors.md` — 14款Core处理器对比（网络I/O/板载I/O/Dante/AEC/VoIP/GPIO/RS232）
- `IO_Expanders/QIO-S4.md` — RS485接线（半双工: RTS=A+, TX=B-）
- `IO_Expanders/` — QIO系列扩展器（GPIO/IR/继电器/音频/24f/ML24i）
- `Control_IO/` — TSC 系列触摸屏（G2/G3）
- `Video/` — NC/NV/NVM/VSA 视频设备
- `Audio_Network_Amps/` — CX-Q/CXD-Q/MPA-Q/SPA-Qf 网络功放
- `Page_Stations/` — 寻呼站

## 工作流 / Workflow

1. **需求整理**: 先列出输入/输出引脚、属性参数、面板页面、行为逻辑，与用户确认
2. **编写 qplug**: 单文件结构，按 PluginInfo → GetProperties → RectifyProperties → GetPages → GetControls → GetControlLayout → 运行时 顺序
3. **归档**: 复制到 `C:\Users\<user>\Documents\QSC\Q-Sys Designer\Plugins\`
4. **测试**: Q-SYS Designer 中拖入组件，检查引脚、面板、运行时日志
5. **发布**: 每个模块独立 GitHub 仓库（命名 `qsys-<kebab-case>`，如 `qsys-crestron-cip`），用户 `xlooong`，中英文双语 README

## 关键规则 / Critical Rules (必须遵守)

- **创建新插件时必须生成唯一 `PluginInfo.Id`**，用 `[guid]::NewGuid().ToString()` (PowerShell) 生成，禁止复制粘贴旧插件的 Id；Id 一旦确定后续版本永远不改，只升 Version
- **每次修改插件内容必须同步升级 `PluginInfo.Version` 版本号**（如 1.0.0→1.0.1 或 1.1.0），Q-SYS Designer 靠版本号判断组件是否需要更新；版本号不升会导致设计文件里的旧组件无法检测到更新，甚至出现"提示更新到更低版本"的异常
- `ButtonType="Trigger"` 的 EventHandler 中 `c.Boolean` 为 false，必须无条件执行
- Knob 必须设 `ControlUnit="Integer"` 才生成外部引脚
- `ButtonStyle` 只影响面板外观，不影响引脚类型
- 修改 `*_count` 属性后必须删除并重新拖入组件
- 面板所有框留足边距，宁大勿小
- 每个插件底部必须有 Notes 中英文说明
- 面板文字全英文，Notes 中英文双语
- 看门狗用 `os.time()`，不要用 `os.clock()`

## 资源 / Resources

- `references/qplug-standards.md` — 完整编写规范与陷阱表
- `references/pitfalls.md` — 18个真实踩坑记录
- `references/wxl-conventions.md` — wxl_personal_plug 插件清单与GitHub仓库映射
- `references/css-uci/` — CSS/UCI 样式开发知识库
- `references/q-sys-10.4-docs/` — Q-SYS 10.4 全站文档知识库（Control_Scripting 34页 + External_Control 5页 + Schematic_Library 65页 + Hardware 24+产品 + CSS/UCI）
- `references/developer-help/` — DeveloperHelp 知识库（Getting_Started + Standards_Definitions + Code_Examples + Recommended_Practices + Books + Community）
- 官方文档: https://help.qsys.com/DeveloperHelp/
- Plugin Compiler: https://help.qsys.com/DeveloperHelp/#Development_Tools/Plugin_Compiler.htm
