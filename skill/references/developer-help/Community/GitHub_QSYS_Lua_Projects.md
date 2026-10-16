# GitHub Q-SYS Lua 开源项目知识库

> 搜索来源: https://github.com/search?q=qsys+language%3ALua&type=repositories
> 共 126 个仓库，筛选优秀项目整理
> 整理时间: 2026-10-12

## 仓库总览

| 仓库 | Stars | 作者 | 核心价值 |
|------|-------|------|---------|
| [locimation/qsys-plugins](https://github.com/locimation/qsys-plugins) | 90 | Michael Goodyear | 最全面的插件集合（Logic/设备控制） |
| [locimation/qsys-http-server](https://github.com/locimation/qsys-http-server) | 12 | Locimation | Q-SYS Lua HTTP 服务器库 |
| [JaumeAP/qsys-plugins](https://github.com/JaumeAP/qsys-plugins) | 12 | Jaume Puig | Dolby 控制 + StateTrigger + MultiFlipFlop |
| [ShinigamiBoss/QSYS-Lua-Module-Extension](https://github.com/ShinigamiBoss/QSYS-Lua-Module-Extension) | 14 | ShinigamiBoss | 外部编辑器 IntelliSense 扩展 |
| [kcx1/Lua_Utilities](https://github.com/kcx1/Lua_Utilities) | 11 | kcx1 | Lua 工具模块库（数学/字符串/表/计算器） |
| [tyler-danielson/QSYS-Home-Assistant](https://github.com/tyler-danielson/QSYS-Home-Assistant) | 10 | tyler-danielson | Home Assistant 集成插件 |
| [morte615/QSYS-Pin-Pad](https://github.com/morte615/QSYS-Pin-Pad) | 8 | Matt Drake | PIN 码密码板 + 超时自动登出 |
| [llamafilm/qsys-plugin-syslog](https://github.com/llamafilm/qsys-plugin-syslog) | 7 | llamafilm | Syslog 消息发送 |
| [isaaacporter/q-sys-plugin-visca-camera](https://github.com/isaaacporter/q-sys-plugin-visca-camera) | 5 | Isaac Porter | VISCA 摄像头多文件工程结构 |
| [llamafilm/qsys-plugin-prometheus-exporter](https://github.com/llamafilm/qsys-plugin-prometheus-exporter) | 6 | llamafilm | Prometheus 指标导出 |
| [shorty456132/qsys-vscode-extension](https://github.com/shorty456132/qsys-vscode-extension) | 26 | shorty456132 | VS Code 扩展（IntelliSense + 代码片段） |

---

## 一、StateTrigger 边沿检测模式（JaumeAP）

**用途**: Boolean 状态变化时触发 Trigger 脉冲，是 Flip-Flop 的逆操作。

```lua
PluginInfo = {
    Name = "Utility~State Trigger",
    Version = "2.0",
    BuildVersion = "2.0.0.3",  -- 新增字段：构建版本号
    Id = "8b93d00a-...",
    Author = "Jaume Puig",
    Description = "...",
}

function GetProperties()
    return {
        { Name = "Channels", Type = "integer", Value = 1, Min = 1, Max = 256 },
        { Name = "Detection", Type = "enum", Choices = { "On", "Off", "Both" }, Value = "Both" },
    }
end

function RectifyProperties(props)
    props.plugin_show_debug.IsHidden = true  -- 隐藏系统调试属性
    return props
end

-- 运行时：边沿检测
for t = 1, Properties["Channels"].Value do
    Controls["State_" .. t].EventHandler = function(ctrl)
        local mode = Properties["Detection"].Value
        local becameActive = Controls["State_" .. t].Boolean  -- 重新读取，不依赖 ctrl 参数
        if mode == "Both" or (mode == "On" and becameActive) or (mode == "Off" and not becameActive) then
            Controls["Out_" .. t]:Trigger()  -- Trigger 按钮的 :Trigger() 方法
        end
    end
end
```

**关键要点**:
- `:Trigger()` 方法可程序化触发 Trigger 按钮
- EventHandler 中**不依赖 `ctrl.Boolean` 参数**，重新从 Controls 读取（Q-SYS 规范）
- `BuildVersion` 字段用于更细粒度的版本追踪
- `RectifyProperties` 中 `props.plugin_show_debug.IsHidden = true` 隐藏调试属性

---

## 二、多文件插件工程结构（isaaacporter/ViscaCamera）

大型插件可拆分为多个 Lua 文件，用 Plugin Compiler 编译为单 .qplug：

```
ViscaCamera/
├── plugin.lua           -- 主入口，require 其他模块
├── info.lua             -- PluginInfo
├── properties.lua       -- GetProperties
├── rectify_properties.lua -- RectifyProperties
├── controls.lua         -- GetControls
├── layout.lua           -- GetControlLayout
├── pages.lua            -- GetPages (动态页面)
├── pins.lua             -- 引脚定义
├── components.lua       -- 嵌入式组件
├── resources.lua        -- 资源（图片/SVG）
├── model.lua            -- 数据模型/状态
├── runtime.lua          -- 运行时逻辑
├── wiring.lua           -- EventHandler 绑定
├── graphics/            -- 图形资源
└── plugincompile/       -- 编译配置
```

**适用场景**: 超过 500 行的复杂插件（如 crestronCIP、RoomAutoSwitch）可考虑拆分。

---

## 三、HTTP Server 库（locimation）

Q-SYS Lua 内置的 HTTP 服务器实现，支持路由、中间件、WebSocket：

```lua
require('http_server')

API = HttpServer.New()
API:use(HttpServer.json())   -- JSON 解析中间件
API:use(HttpServer.cors())   -- CORS 中间件

API:get('/greeting', function(req, res)
    res.send('Hello world!')
end)

API:post('/control', function(req, res)
    -- req.body 已被 json 中间件解析
    res.send({ status = "ok" })
end)

API:listen(9091)
```

**可用 API**:
- `HttpServer.New()` — 创建实例
- `server:use(middleware)` — 中间件
- `server:get/post/put/delete/all(path, handler)` — 路由
- `server:ws(path, handler)` — WebSocket（仅服务端→客户端）
- `HttpServer.Static(root)` — 静态文件服务

**应用**: 可用于 crestronCIP 的 Web 监控界面替代 TCP log server。

---

## 四、PIN Pad 超时模式（morte615）

密码输入 + 活动超时自动登出：

```lua
-- 属性
{ Name = "Number of PINs", Type = "integer", Min = 1, Max = 100, Value = 1 },
{ Name = "Log Entries", Type = "boolean", Value = true },

-- 控件
{ Name = "code", ControlType = "Text", PinStyle = "Input" },
{ Name = "Touch Activity", ControlType = "Indicator", IndicatorType = "LED", PinStyle = "Input", UserPin = true },
{ Name = "PinNum", ControlType = "Button", ButtonType = "Trigger", Count = 10, UserPin = true },
{ Name = "Reset", ControlType = "Button", ButtonType = "Trigger", UserPin = true },
{ Name = "Submit", ControlType = "Button", ButtonType = "Trigger", UserPin = true },
{ Name = "Logoff", ControlType = "Button", ButtonType = "Trigger", UserPin = true, IconType = "Image" },
```

**关键模式**:
- `Touch Activity` 输入引脚检测用户活动，超时计时器重置
- 超时时间可配，0 = 禁用
- PIN 验证通过后跳转到指定页面
- 日志记录成功/失败尝试

---

## 五、Lua 工具模块库（kcx1）

可复用的 Lua 模块集合：

| 模块 | 功能 |
|------|------|
| `Utilities.lua` | 通用工具函数 |
| `Advanced_Math.lua` | 高级数学运算 |
| `Advanced_String.lua` | 字符串高级处理 |
| `Advanced_Tables.lua` | 表操作扩展 |
| `Calculators.lua` | 计算器函数 |

**使用方式**: 在 Q-SYS 脚本中 `require("Utilities")` 引入。

---

## 六、VS Code 开发环境

### 扩展: shorty456132/lua-for-qsys (v1.3.0)

- IntelliSense 代码补全
- 代码片段关键词: `ctrl`, `ctrl.Button`, `ctrl.Knob`, `ctrl.Indicator`, `prop`, `components`, `graphics`, `layout`, `GroupBox`
- 建议编写 Controls/Properties/Layout 时暂停其他补全插件

### 外部编辑器: ShinigamiBoss/QSYS-Lua-Module-Extension

- 单个 `QSYS Lua Extension.lua` 文件
- 在外部编辑器中 `require` 后获得完整 Q-SYS API 的 IntelliSense
- 每个函数都有描述注释

---

## 七、可复用设计模式汇总

### 7.1 边沿检测（State→Trigger）
```lua
Controls.Input.EventHandler = function()
    local current = Controls.Input.Boolean
    if current ~= lastState then
        lastState = current
        Controls.Output:Trigger()
    end
end
```

### 7.2 互斥组（MultiFlipFlop Exclusive 模式）
```lua
-- 点击一个时关闭其他所有
for i = 1, count do
    Controls["Btn_" .. i].EventHandler = function()
        for j = 1, count do
            if j ~= i then Controls["Btn_" .. j].Boolean = false end
        end
    end
end
```

### 7.3 活动超时（Retriggerable One Shot 的 Lua 实现）
```lua
local timeoutTimer = Timer.New()
local active = false
timeoutTimer.EventHandler = function()
    active = false
    Controls.LoggedIn.Boolean = false
end

Controls.Activity.EventHandler = function()
    if Controls.Activity.Boolean then
        active = true
        timeoutTimer:Start(timeoutSeconds)  -- 重新计时
    end
end
```

### 7.4 Trigger 程序化触发
```lua
Controls.MyTrigger:Trigger()  -- 不需要设置 Boolean，直接调用方法
```

### 7.5 隐藏系统调试属性
```lua
function RectifyProperties(props)
    props.plugin_show_debug.IsHidden = true
    return props
end
```

### 7.6 版本号双字段
```lua
PluginInfo = {
    Version = "2.0",          -- 主版本（Q-SYS 判断更新）
    BuildVersion = "2.0.0.3", -- 构建版本（细粒度追踪）
}
```

---

## 八、与 wxl_personal_plug 的对比与改进

| 方面 | 社区最佳实践 | 我们的现状 | 改进建议 |
|------|-------------|-----------|---------|
| PluginInfo.Id | UUID ✅ | 部分缺失 | **全部加 UUID** |
| BuildVersion | 双版本号 | 未使用 | 复杂插件可加 |
| RectifyProperties | 隐藏 debug 属性 | 未使用 | 加入 |
| :Trigger() 方法 | 程序化触发 | 部分使用 | 全部统一 |
| 边沿检测模式 | StateTrigger 模式 | 手写 | 参考标准化 |
| 互斥组 | MultiFlipFlop Exclusive | 手写 | 参考标准化 |
| 多文件结构 | Plugin Compiler | 单文件 | crestronCIP 可考虑拆分 |
| HTTP Server | locimation 库 | 未使用 | 可替代 TCP log |
| 活动超时 | PIN Pad 模式 | 手写 | 参考标准化 |
| 外部 IntelliSense | VS Code 扩展 + Lua Extension | 已安装 VS Code 扩展 | 可加 Lua Extension 文件 |

---

## 九、值得深入学习的源码

| 仓库/文件 | 学习点 |
|-----------|--------|
| JaumeAP/StateTrigger.qplug | 边沿检测、:Trigger()、RectifyProperties 隐藏 debug |
| JaumeAP/MultiFlip-Flop.qplug | 互斥组、多通道状态输出 |
| locimation/Logic/Stepper.lua | 定时器驱动步进序列 |
| locimation/Logic/FSM.lua | 有限状态机、LOCKOUT 防重入 |
| locimation/qsys-http-server/init.lua | HTTP 服务器实现 |
| morte615/Pin Pad.qplug | 超时登出、密码验证 |
| isaaacporter/ViscaCamera/ | 多文件工程结构 |
| kcx1/Utilities.lua | 可复用工具函数 |
