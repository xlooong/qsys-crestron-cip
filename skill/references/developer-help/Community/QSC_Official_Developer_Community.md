# Q-SYS 官方开发者社区 GitHub 知识库

> 来源: https://github.com/Q-SYS-Communities-for-Developers
> 官方组织，73 followers，11 个仓库
> 整理时间: 2026-10-12
> 官网: https://developers.qsc.com/s/

## 仓库总览

| 仓库 | Stars | 核心内容 | 学习价值 |
|------|-------|---------|---------|
| [reference-files](https://github.com/Q-SYS-Communities-for-Developers/reference-files) | 31 | CSS参考/计算用量/动态图标/Lua模块 | ⭐⭐⭐⭐⭐ |
| [Plugin-Evaluation-Script](https://github.com/Q-SYS-Communities-for-Developers/Plugin-Evaluation-Script) | 11 | 插件设计时代码评估脚本 | ⭐⭐⭐⭐⭐ (已入库) |
| [command-txrx-examples](https://github.com/Q-SYS-Communities-for-Developers/command-txrx-examples) | 9 | Command Send/Receive 插件教程(TCP+HTTP) | ⭐⭐⭐⭐ |
| [uci-scripting](https://github.com/Q-SYS-Communities-for-Developers/uci-scripting) | 5 | 脚本通知/中央广播/多房间控制 | ⭐⭐⭐⭐ |
| [Communities-Webinars](https://github.com/Q-SYS-Communities-for-Developers/Communities-Webinars) | 5 | UI/UX 设计网络研讨会 | ⭐⭐⭐ |
| [System-Customization](https://github.com/Q-SYS-Communities-for-Developers/System-Customization) | 3 | 房间定制/多语言UCI/组件选择 | ⭐⭐⭐⭐ |
| [Language-Translation](https://github.com/Q-SYS-Communities-for-Developers/Language-Translation) | 0 | DeepL API 自动翻译 | ⭐⭐⭐ |
| [Sequencing-and-Timing](https://github.com/Q-SYS-Communities-for-Developers/Sequencing-and-Timing) | 0 | Sequencer + When 组件/30语言翻译 | ⭐⭐⭐ |
| [Flexbox](https://github.com/Q-SYS-Communities-for-Developers/Flexbox) | 1 | Flexbox CSS 布局 | ⭐⭐⭐ |
| [smart-dollhouse](https://github.com/Q-SYS-Communities-for-Developers/smart-dollhouse) | 2 | 入门项目：娃娃屋控制 | ⭐⭐ |

---

## 一、reference-files（最受欢迎，31⭐）

### 1.1 CSS Reference
- 完整的 UCI 控件样式参考
- 包含多种自定义控件样式示例
- 分段仪表（segmented gauge）
- Flexbox 布局示例
- Layer style faders 的 pressed 选项
- **用途**: 复制粘贴样式元素，快速创建自定义面板

### 1.2 Compute Usage（计算用量监控）
- 监控 Core 的计算资源使用
- 可作为 User Component 拖入设计
- 需要 Core Status 块启用 verbose 模式
- **用途**: 故障排查 + 功能扩展时的性能护栏

### 1.3 Lua Modules（Lua 模块导入）
- 演示如何在脚本中 `require` Lua 模块
- 3 个模块示例：
  - 2 个官方编写的模块
  - 1 个从 GitHub 下载的 Lorem Ipsum 生成器
  - 1 个 DeepL 翻译模块（需要 API key）
- **关键**: Lua 模块必须通过 Design Resources 标签添加到设计中
- **用途**: 代码复用，避免重复造轮子

### 1.4 Dynamic Icons（动态图标）
- Base64 编码图片存储在 Core 上
- 通过 LED 控件更新图标
- ComboBox 选择时切换图标
- **用途**: 自定义 UCI 中的动态视觉反馈

---

## 二、command-txrx-examples（9⭐）

Command Send and Receive Utility Plugin 的教程文件。

### 2.1 TCP 示例
- 使用 Command TxRx Utility 通过 TCP 发送命令
- 接收命令更新实时反馈
- 包含编程挑战练习

### 2.2 HTTP 示例（Postman Echo）
- 使用 Command TxRx Utility 的 HTTP 模式
- 通过 Postman Echo API 测试 HTTP 请求
- **关键发现**: 可以用 Command Send/Receive Plugin 连接到 Named Controls

### 对我们的价值
- AtlonaUsbSwitch、Extron SW2、CrestronViscaCamera 等 TCP 控制插件可参考此模式
- HTTP 模式可用于 REST API 设备控制

---

## 三、uci-scripting（5⭐）

### 3.1 Script Notifications（脚本通知）
- 中央脚本发布系统级公告
- Code Pins 保持脚本间同步
- 双向脚本通知用于房间控制
- 组件选择（Component Selection）分组控件
- JSON 格式字符串用于房间配置

### 3.2 配置文件
- `announcement-config.json` — 公告配置示例
- `template-config.json` — 房间控制配置示例

### 对我们的价值
- 多房间系统（RoomCombineSync、RoomUserModeSelector）可使用 Notifications 实现跨脚本通信
- JSON 配置文件模式可用于房间模板

---

## 四、System-Customization（3⭐）

### 4.1 房间定制系统
- 现场可调整的控件，适应房间差异
- 房间控制脚本处理系统自动化
- 用户选择哪些组件需要被控制
- 每个房间独立调整（如运动传感器超时）

### 4.2 多语言 UCI
- UCI 文本辅助脚本接收 JSON 字符串填充面板文字
- ComboBox 切换语言
- 已包含 6 种语言：中文/德语/英语/法语/葡萄牙语/西班牙语

### 4.3 三种 UCI 实现对比
1. **"No Code"** — 几乎全部用 Control Pins
2. **Component Controls** — 用组件控件做房间和文本控制
3. **Script Notifications** — 进一步集成脚本通知

### 对我们的价值
- 多语言支持模式可用于 crestronCIP 等插件的国际化
- 房间定制模式适用于 RoomAutoSwitch 的现场配置

---

## 五、Sequencing-and-Timing

### 5.1 Sequencer + When 组件
- Sequencer 组件基础用法
- When + Sequencer 组合控制系统开关机宏
- Admin Controls UCI 配置定时事件
- 每个事件可独立启用/禁用（用 Super Buffer 插件）

### 5.2 时间处理技巧
- When 组件的时间控件是 24 小时制
- UCI 脚本将时间拆分为独立的 时/分/AM-PM 下拉框

### 5.3 30 语言翻译
- 使用 LanguageTranslation Lua 模块
- DeepL API 自动翻译为 30 种语言

### 对我们的价值
- System On-Off Timer 可参考 Sequencer/When 的时间处理模式
- 开关机定时的 UI 设计参考

---

## 六、官方推荐的开发模式

### 6.1 教程文件结构
所有官方教程文件遵循统一结构：
```
00 Instructions  — 使用说明
01 Demo          — 功能演示
02 Example       — 完整示例
03 Challenge     — 编程挑战
```

### 6.2 作者团队
- **Hope Roth** (@qsc-hoperoth) — 主要教程作者
- **Eugene Dunn III** (@qsc-eugene) — QA 支持
- **Thomas Holt-Ronczy** — 分段仪表/测试

### 6.3 版本依赖
- reference-files: Q-SYS Designer 9.12+
- command-txrx: Q-SYS Designer 9.5+
- uci-scripting: Q-SYS Designer 9.12+
- System-Customization: Q-SYS Designer 9.12+
- Sequencing: Q-SYS Designer 10.0+

---

## 七、可直接应用到 wxl_personal_plug 的模式

### 7.1 Compute Usage 监控
可在 crestronCIP 等资源密集型插件中加入计算用量监控，防止 Core 过载。

### 7.2 Lua 模块复用
将通用函数（如 hex 转换、时间解析）抽为 Lua 模块，通过 Design Resources 引入。

### 7.3 Script Notifications 多房间通信
RoomCombineSync + RoomUserModeSelector + RoomAutoSwitch 之间可用 Notifications 同步状态，避免硬连线。

### 7.4 动态图标
用 Base64 图片 + LED 控件实现插件面板的自定义图标（如连接状态图标）。

### 7.5 多语言支持
参考 System-Customization 的 JSON 配置模式，为插件面板添加中英文切换。

### 7.6 Command TxRx 替代手写 TCP
对于简单的 TCP/HTTP 设备控制，可考虑用官方 Command Send/Receive Plugin 替代手写 TcpSocket 代码。

---

## 八、与社区开源项目的互补

| 方面 | 官方社区 | 社区开源 |
|------|---------|---------|
| 教程质量 | ⭐⭐⭐⭐⭐ 结构化教程 | ⭐⭐⭐ 代码示例为主 |
| 插件数量 | 少（教程为主） | 多（实际设备插件） |
| CSS/UCI | ⭐⭐⭐⭐⭐ 完整参考 | ⭐⭐ 较少 |
| TCP/HTTP 模式 | Command TxRx 教程 | 手写 TcpSocket 实例 |
| 多房间/通知 | ⭐⭐⭐⭐ 完整教程 | ⭐⭐ 较少 |
| 设备控制插件 | 少 | ⭐⭐⭐⭐ 丰富 |

**建议**: 官方教程学架构和模式，社区开源学具体设备实现。
