# qplug 文件结构模板

## 完整文件骨架

```lua
--==============================================================================
-- PluginName.qplug
-- Version: 1.0.0
-- Author: yourname
-- Category: category~PluginName
--==============================================================================

-- Required metadata (read by Q-SYS Designer)
PluginInfo = {
  Name = "PluginName",
  Version = "1.0.0",
  Author = "yourname",
  Category = "my_series~PluginName",
  Description = "Short description"
}

--==============================================================================
-- 1. Properties (shown in Designer Properties panel)
--==============================================================================
function GetProperties()
  local props = {}
  table.insert(props, {
    Name = "param_name",
    Type = "string",       -- string | double | int | bool
    Value = "default"
  })
  table.insert(props, {
    Name = "count",
    Type = "double",
    Min = 1,
    Max = 500,
    Value = 32
  })
  return props
end

--==============================================================================
-- 2. Controls (define all pins and UI elements)
--==============================================================================
function GetControls(props)
  local ctrls = {}
  local count = math.floor(props["count"].Value)

  -- Static controls (always present)
  table.insert(ctrls, {
    Name = "Enable",
    ControlType = "Button",
    ButtonType = "Toggle",
    DefaultValue = false,
    PinStyle = "Input",
    UserPin = true,
    Count = 1
  })

  -- Dynamic controls (count-based)
  for i = 1, count do
    table.insert(ctrls, {
      Name = "Digital_In_" .. i,
      ControlType = "Button",
      ButtonType = "Toggle",
      DefaultValue = false,
      PinStyle = "Output",
      UserPin = true,
      Count = 1
    })
    table.insert(ctrls, {
      Name = "Analog_In_" .. i,
      ControlType = "Knob",
      ControlUnit = "Integer",  -- REQUIRED for Knob pins to appear!
      Min = 0,
      Max = 65535,
      DefaultValue = 0,
      PinStyle = "Output",
      UserPin = true,
      Count = 1
    })
  end

  -- UI-only controls (no external pin)
  table.insert(ctrls, {
    Name = "Status_Text",
    ControlType = "Text",
    DefaultValue = "Idle",
    UserPin = false,
    Count = 1
    -- NO PinStyle when UserPin=false!
  })

  return ctrls
end

--==============================================================================
-- 3. Pages (panel tab names)
--==============================================================================
function GetPages(props)
  return {
    { name = "Main" },
    { name = "Settings" }
  }
end

--==============================================================================
-- 4. Control Layout (panel graphics and positioning)
--==============================================================================
function GetControlLayout(props, CurrentPage)
  local graphics = {}
  local layout = {}
  local fs = 12

  if CurrentPage.name == "Main" then
    -- GroupBox
    table.insert(graphics, {
      Type = "GroupBox",
      Text = "Status",
      FontSize = fs,
      Position = {8, 8},
      Size = {324, 200}
    })
    -- Control placement
    layout["Enable"] = {
      PrettyName = "Enable",
      Legend = "Enable",
      Style = "Button",
      ButtonStyle = "Toggle",
      Position = {20, 40},
      Size = {100, 30}
    }
  end

  return graphics, layout
end

--==============================================================================
-- 5. Runtime (executes on Core)
--==============================================================================
-- State variables
local isRunning = false
local mainTimer = Timer.New()

-- Event handlers
Controls.Enable.EventHandler = function(c)
  if c.Boolean then
    isRunning = true
    mainTimer:Start(1)
  else
    isRunning = false
    mainTimer:Stop()
  end
end

mainTimer.EventHandler = function()
  -- periodic logic
end

-- Startup
print("PluginName started")
```

## 各函数要点

### GetProperties
- Type 支持：`string`, `double`, `int`, `bool`
- double/int 支持 Min/Max
- string 类型 Value 是默认值
- 运行时通过 `Properties["name"].Value` 读取

### GetControls
- 每个控件必须有唯一 Name
- ControlType 决定控件类型（见 control-types.md）
- PinStyle: `"Input"` 或 `"Output"`，决定引脚方向
- UserPin: `true` 显示在外部引脚，`false` 仅面板内部使用
- **Knob 必须加 `ControlUnit = "Integer"`**

### GetPages
- 返回 `{name = "页面名"}` 表数组
- 页面顺序即标签页顺序

### GetControlLayout
- 返回两个值：`graphics`（静态图形）和 `layout`（控件位置）
- graphics 类型：GroupBox, Text, Line, Rectangle
- layout 中每个控件通过 Name 匹配 GetControls 中的定义
- Position = {x, y}, Size = {w, h}

### 运行时
- 所有代码在文件底部，不在函数内
- Timer: `Timer.New()`, `:Start(seconds)`, `:Stop()`, `.EventHandler`
- TCP: `TcpSocket.New()`, `:Connect(ip, port)`, `:Write(data)`, `:Read(bytes)`, `.EventHandler`
- 控件访问：`Controls["Name"]` 或 `Controls.Name`
- 属性访问：`Properties["name"].Value`
