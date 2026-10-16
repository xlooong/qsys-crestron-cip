# Q-SYS DeveloperHelp Knowledge Base

> 来源: https://help.qsys.com/DeveloperHelp/
> 抓取时间: 2026-10-12（缺失页补抓: 2026-10-16，全部 27 页补齐）
> 用途: qplug 插件开发参考知识库
> 已抓取: 43 个页面

## 目录结构 / Directory

### Getting_Started/ - 入门指南

| 文件 | 说明 | 状态 |
|------|------|------|
| Q-SYS_Core_OS_Environment_Overview.md | Core OS 环境概览（Audio/Runtime引擎、Lua 5.3、30fps控制帧） | ✅ 完整 |
| Script_vs_Plugin_Determination.md | Script 与 Plugin 的区别与选择 | ✅ 完整 |
| Building_a_Plugin.md | 构建插件的两种方式（手动/编译器） | ✅ 完整 |

### Standards_Definitions/ - 标准与定义

| 文件 | 说明 | 状态 |
|------|------|------|
| Style_Guide.md | 代码风格指南 | ✅ 完整 |
| Reserved_Control_Names.md | 保留控件名（Status、IPAddress、Port等） | ✅ 完整 |
| Reserved_Functions.md | 保留函数（GetProperties/GetControls/GetControlLayout等） | ✅ 完整 |
| Embedded_Components.md | 嵌入式组件 | ✅ 完整 |
| Notifications_API.md | Q-SYS Lua 通知 API | ✅ 完整 |
| Reserved_Notifications_Names.md | 保留通知名 | ✅ 完整 |

### Development_Tools/ - 开发工具

| 文件 | 说明 | 状态 |
|------|------|------|
| Plugin_Compiler.md | 插件编译器（VS Code + Git，多文件编译为单qplug） | ✅ 完整 |
| Plugin_Encryption_Tool.md | 插件加密工具 | ✅ 完整 |

### Tools/ - 社区工具

| 文件 | 说明 | 状态 |
|------|------|------|
| Plugin_Evaluation_Script.md | 插件评估脚本（SDK标准校验、语法检查、JSON报告） | ✅ 完整 |

### Books/ - 书籍与教程

| 文件 | 说明 | 状态 |
|------|------|------|
| Lua_Scripting_in_Q-Sys.md | 《Lua Scripting in Q-Sys》Aaron Hood / The Farm AV，31页完整指南（Lua基础+Q-Sys扩展+Text Controller构建+高级概念） | ✅ 完整 |

### Community/ - 社区开源项目学习

| 文件 | 说明 | 状态 |
|------|------|------|
| Locimation_qsys-plugins_Study.md | Locimation qsys-plugins 库学习笔记（90星），14个代码模式+与wxl_personal_plug对比+可复用模式 | ✅ 完整 |
| GitHub_QSYS_Lua_Projects.md | GitHub 126个Q-SYS Lua仓库筛选，11个优秀项目总览+7个可复用设计模式+对比改进建议 | ✅ 完整 |
| QSC_Official_Developer_Community.md | Q-SYS官方开发者社区11个仓库详解（reference-files/command-txrx/uci-scripting等）+7个可应用模式 | ✅ 完整 |

### Code_Examples/ - 代码示例

| 文件 | 说明 | 状态 |
|------|------|------|
| Basic_Plugin_Framework.md | 基础插件框架（PluginInfo/GetColor/GetProperties/GetControls/GetControlLayout） | ✅ 完整 |
| Dynamic_Pages.md | 动态页面（GetDynamicPages，根据属性显示/隐藏页面） | ✅ 完整 |
| Hex_Data_Handling.md | Hex/二进制数据处理（hex2str/str2hex/hex2num/num2hex） | ✅ 完整 |
| Plugin_Property_Headers_Comments.md | 属性 Header 和 Comment（v9.10+） | ✅ 完整 |
| TCPSocket_Example.md | TCP Socket 示例 | ✅ 完整 |
| TCPSocket_Debugging.md | TCP Socket 调试 | ✅ 完整 |
| Telnet_Example.md | Telnet 示例（登录/认证/重连） | ✅ 完整 |
| UDPSocket_Example.md | UDP Socket 示例（单播/组播/NIC选择） | ✅ 完整 |
| Serial_Server_Serial_Client.md | 串口服务端/客户端示例 | ✅ 完整 |
| SerialPort.md | 串口使用示例 | ✅ 完整 |
| HTTPClient.md | HTTP 客户端示例（GET/POST/Download/Upload） | ✅ 完整 |
| JSON_Example.md | JSON 编解码示例（rapidjson） | ✅ 完整 |
| XML_Example.md | XML 解析示例（LuaXML） | ✅ 完整 |
| SSH_Example.md | SSH 客户端示例 | ✅ 完整 |
| Crypto_Example.md | 加密对象示例 | ✅ 完整 |
| mDNS_Example.md | mDNS 客户端模块 | ✅ 完整 |
| Named_Components_Example.md | 命名组件示例 | ✅ 完整 |
| Notifications_Example.md | 通知示例 | ✅ 完整 |
| Queue_and_Stack_class.md | 队列和栈类 | ✅ 完整 |
| Storing_Secrets_in_Plugins.md | 插件中存储密钥 | ✅ 完整 |
| Wake_On_LAN_Example.md | 网络唤醒示例 | ✅ 完整 |

### Recommended_Practices/ - 最佳实践

| 文件 | 说明 | 状态 |
|------|------|------|
| TCP.md | TCP 最佳实践（ReadTimeout/WriteTimeout/ReconnectTimeout/IsConnected） | ✅ 完整 |
| UDP.md | UDP 最佳实践（单播/双向/组播/全局声明） | ✅ 完整 |
| Serial.md | 串口最佳实践 | ✅ 完整 |
| LuaScoping.md | Lua 作用域 | ✅ 完整 |
| Pcall.md | pcall 错误处理 | ✅ 完整 |
| Plugin_Debug.md | 插件调试方法（print/Show Debug属性/连接状态日志） | ✅ 完整 |

## 核心要点速查 / Key Points

### PluginInfo 结构
```lua
PluginInfo = {
  Name = "Plugin Name",
  Version = "1.0.0",
  BuildVersion = "1.0.0",
  Id = "unique_plugin_id",
  Author = "Author Name",
  Description = "Plugin description"
}
```

### 必需的设计时函数
- `GetProperties()` - 定义属性
- `RectifyProperties(props)` - 属性变更后调整（可选）
- `GetControls(props)` - 定义控件
- `GetControlLayout(props)` - 定义面板布局，返回 (layout, graphics)
- `GetPages(props)` - 定义页面（可选）
- `GetColor(props)` - 组件颜色（可选）
- `GetPrettyName(props)` - 组件显示名（可选）

### 属性类型
- `string` - 字符串
- `integer` - 整数（需 Min/Max/Value）
- `double` - 浮点数
- `boolean` - 是/否（运行时返回 true/false）
- `enum` - 下拉选择（需 Choices）

### 属性 Header 和 Comment（v9.10+）
```lua
{
  Name = "Input Count",
  Type = "integer",
  Value = 8,
  Min = 2,
  Max = 32,
  Comment = "Range: 2-32",
  Header = "Channels"
}
```

### 控件类型
- Button: Toggle / Momentary / Trigger / StateTrigger / On / Off / Custom
- Knob: 各种单位（Integer/Float/Percent/Level等）
- Text: Text Edit / Text Display
- Indicator: LED / Status Display
- Meter / Fader / Combo

### TCP Socket 最佳实践
- `.ReadTimeout` - 读超时（0=禁用，默认0），应大于轮询速率
- `.WriteTimeout` - 写超时（0=禁用，默认0）
- `.ReconnectTimeout` - 重连间隔（0=禁用，默认5秒）
- `.IsConnected` - 只读，发送前检查
- `.BufferLength` - 只读，缓冲区长度

### UDP Socket 最佳实践
- 必须全局声明，防止垃圾回收
- 单向通信: `udp:Open()` 无参数
- 双向通信: 需绑定本地端口
- 组播: `udp:JoinMulticast(address)`

### Hex 数据处理
```lua
function hex2str(str) return str:gsub(".", function(b) return string.format("%02X", string.byte(b)) end) end
function str2hex(str) return str:gsub("..", function(b) return string.char(tonumber(b,16)) end) end
```

### 调试方法
- 运行时开始打印 `PluginInfo.Version`
- 连接状态变化必须打印
- 所有插件自动获得 "Show Debug" 属性（默认 No）
- 收发数据可通过属性或控件控制是否打印

### Core OS 环境
- Lua 5.3，大部分标准库可用
- Runtime engine 30fps 处理控制变化
- 控制值每33ms传输到DSP系数
- 所有 Lua 脚本单线程共享资源
- Audio engine 3000fps 处理音频
