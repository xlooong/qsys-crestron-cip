# Reserved Functions（保留函数完整定义）

> 来源: Q-SYS Developer Help - Standards and Definitions - Reserved Functions（27页）
> 本地文件: `C:\Users\longe\Desktop\Q-SYS 文档\qplug\7. Standards and Definitions - Reserved Functions.pdf`
> 整理时间: 2026-10-13

> **注意**: Lua 区分大小写，例如 "string" 和 "String" 不同。

---

## 一、设计时函数 / Design Time Functions

### 1. GetPrettyName(props) — 可选

返回组件拖入设计时显示的名称。不指定则显示 PluginInfo 中的 Name。属性值可通过传入的 props 表访问。

| 返回类型 | 必填 | 说明 |
|----------|------|------|
| String | 否 | 组件在原理图上显示的名称 |

```lua
function GetPrettyName(props)
  return string.format("My Plugin Name %s", PluginInfo.Version)
end
```

> **Tip**: 可通过 `PluginInfo.Version` 包含版本信息。

---

### 2. GetColor(props) — 可选

返回组件添加到设计时的初始颜色。颜色为三个 0-255 整数组成的表 `{Red, Green, Blue}`。

| 属性 | 类型 | 必填 | 说明 |
|------|------|------|------|
| Red | Integer | 是 | 红色强度 0-255 |
| Green | Integer | 是 | 绿色强度 0-255 |
| Blue | Integer | 是 | 蓝色强度 0-255 |

```lua
function GetColor(props)
  return { 102, 102, 102 }
end
```

---

### 3. GetProperties() — **必填**

添加插件属性。这些是用户可配置字段，在设计时的属性窗口中显示。每个属性是一个对象，支持以下参数：

| 属性 | 类型 | 必填 | 说明 |
|------|------|------|------|
| Name | String | 是 | 属性名称（在 QDS 属性面板显示） |
| Type | String | 是 | 属性类型："string" / "integer" / "double" / "boolean" / "enum" |
| Value | Varies | 是 | 默认值（类型依赖于 Type） |
| Choices | Table | 否 | enum 类型的选项列表，如 `{"Choice 1", "Choice 2"}` |
| Min | Integer | 否 | 最小值（integer/double 类型） |
| Max | Integer | 否 | 最大值（integer/double 类型） |
| Header | String | 否 | 属性下方显示的标题（QDS 9.10+） |
| Comment | String | 否 | 属性下方显示的注释（QDS 9.10+） |
| Description | String | 否 | 属性简要描述 |

#### Type Properties 类型说明

| Type | 说明 |
|------|------|
| string | 字符串，默认值可选 |
| integer | 有符号长整数，默认值必填 |
| double | 双精度浮点，默认值必填 |
| boolean | 下拉框 "Yes"/"No"，运行时返回 true/false |
| enum | 字符串下拉框（由 Choices 定义），默认值可选（未选时显示空白） |

```lua
function GetProperties()
  local properties = {}
  table.insert(properties,{
    Name = "String Property",
    Type = "string",
    Value = "This is a string"
  })
  table.insert(properties,{
    Name = "Integer Property",
    Type = "integer",
    Min = 0,
    Max = 100,
    Value = 50
  })
  table.insert(properties,{
    Name = "Enum Property",
    Type = "enum",
    Choices = {"Choice1", "Choice2", "Choice3"},
    Value = "Choice 1"
  })
  table.insert(properties,{
    Name = "Bool Property",
    Type = "boolean",
    Value = true
  })
  return properties
end
```

#### 访问属性 / Accessing Properties

属性的当前值会作为参数传入其他保留函数。运行时通过全局 `Properties` 表访问，以属性名为键：

```lua
myValue = Properties["Property Name"].Value  -- 所有属性类型通用
```

---

### 4. RectifyProperties(props) — 可选

属性变更后运行，用于调整全局变量和属性可见性。

| 属性 | 类型 | 必填 | 说明 |
|------|------|------|------|
| IsHidden | Boolean | 否 | 定义属性在 QDS 属性面板中的可见性 |

```lua
function RectifyProperties(props)
  props["Number of PINs"].IsHidden = props["Use PIN"].Value == "No"
  return props
end
```

---

### 5. GetPages(props) — 可选

多页面 UI 时使用。返回页面对象表，每个对象必须包含 `name` 属性。

| 属性 | 类型 | 必填 | 说明 |
|------|------|------|------|
| name | String | 是 | 页面名称 |

> **Tip**: 页面按返回表中的顺序排列。

```lua
PageNames = { "Control", "Setup" }
function GetPages(props)
  local pages = {}
  for ix,name in ipairs(PageNames) do
    table.insert(pages, {name = PageNames[ix]})
  end
  return pages
end
```

> **Note**: PageNames 定义在 GetPages() 外部以便在其他地方访问。可在 GetPages() 内根据属性设置修改，但它仅是常量，修改不会传递到其他 UI 函数。

---

### 6. GetControls(props) — **必填**

返回插件中使用的控件对象表。控件是存储在设计中的持久数据对象，可绑定到用户界面组件和插件引脚。

#### 通用控件属性 / Common Control Properties

| 属性 | 类型 | 必填 | 说明 |
|------|------|------|------|
| Name | String | 是 | 控件名称 |
| ControlType | String | 是 | "Button" / "Knob" / "Indicator" / "Text" |
| DefaultValue | Varies | 否 | 首次编译时的默认值（Boolean/value/string） |
| UserPin | Boolean | 否 | 默认 false。true 时引脚在 QDS "Control Pins" 中可用 |
| PinStyle | String | 否 | 引脚暴露样式："Input" / "Output" / "Both" / "None"。不定义且 UserPin=true 时始终可见 |
| Count | Integer | 否 | 默认 1。>1 时运行时控件以数组形式访问（1-indexed） |

> **Note**: Text 控件无特定属性。可在 GetControlLayout() 中定义 Text 控件是文本框、下拉框还是列表框。

#### Button 特定属性 / Button-Specific Properties

| 属性 | 类型 | 必填 | 说明 |
|------|------|------|------|
| ButtonType | String | 是 | "Toggle" / "Momentary" / "Trigger" / "StateTrigger" |
| Icon | String | 否 | 控件图标（QDS 内置或本地文件，支持 SVG/PNG/JPG） |
| IconType | String | 条件必填 | 图标格式："Icon"（默认）/ "Image" / "Svg" |
| Max | Integer | 条件必填 | StateTrigger 的最大值（ButtonType=StateTrigger 时） |
| Min | Integer | 条件必填 | StateTrigger 的最小值 |

#### Knob 特定属性 / Knob-Specific Properties

| 属性 | 类型 | 必填 | 说明 |
|------|------|------|------|
| ControlUnit | String | 是 | "dB" / "Hz" / "Float" / "Integer" / "Pan" / "Percent" / "Position" / "Seconds" |
| Max | Integer | 条件必填 | 旋钮最大值（必须大于 Min） |
| Min | Integer | 条件必填 | 旋钮最小值（必须小于 Max） |

> **关键**: Knob 必须设 `ControlUnit = "Integer"` 才会生成外部引脚！

#### Knob 范围 / Knob-Specific Ranges

| Control Unit | Lower Limit | Upper Limit | Default Min | Default Max | Min/Max Required |
|--------------|-------------|-------------|-------------|-------------|-----------------|
| dB | -100 | 20 | -100 | 20 | Yes |
| Hz | 20 | 20000 | 20 | 20000 | Yes |
| Float | -1,000,000,000 | 1,000,000,000 | 0 | 100 | Yes |
| Integer | -999,999,999 | 999,999,999 | 1 | 100 | Yes |
| Pan | -1 | 1 | -1 | 1 | No |
| Percent | 0 | 100 | 0 | 100 | Yes |
| Position | 0 | 1 | 0 | 1 | No |
| Seconds | 0 | 87400 | 0 | 1 | Yes |

#### Indicator 特定属性 / Indicator-Specific Properties

| 属性 | 类型 | 必填 | 说明 |
|------|------|------|------|
| IndicatorType | String | 是 | "Led" / "Meter" / "Text" / "Status" |

```lua
function GetControls(props)
  local controls = {}
  -- 单个控件
  table.insert(controls,{
    Name = "TextBox",
    ControlType = "text",
    UserPin = false,
    Count = 1
  })
  -- 多个控件（Count > 1）
  table.insert(controls,{
    Name = "LED Indicator",
    ControlType = "indicator",
    IndicatorType = "Led",
    UserPin = true,
    PinStyle = "Output",
    Count = 5
  })
  return controls
end
```

---

### 7. GetControlLayout(props) — **必填**

返回定义插件 UI 视图的 layout 和 graphics 两个表。

#### Layout Table Properties（控件布局）

| 属性 | 类型 | 必填 | 说明 |
|------|------|------|------|
| Position | Table | 是 | 控件位置 `{x,y}` |
| Size | Table | 是 | 控件尺寸 `{x,y}` |
| Style | String | 是 | 显示样式："Fader" / "Knob" / "Button" / "Text" / "Meter" / "Led" / "ListBox" / "ComboBox" / "Media" / "None"（隐藏控件但保留引脚） |
| ClassName | String | 否 | 拖入 UCI 时的默认 CSS 类名 |
| Color | Table | 否 | 控件颜色 `{r,g,b,alpha}`，alpha 可选 0-255 |
| TextColor | Table | 否 | 文本颜色 `{r,g,b,alpha}` |
| Font | String | 否 | 默认 "Roboto" |
| FontSize | Integer | 否 | 文本字号 |
| FontStyle | String | 否 | 字体样式 |
| IsBold | Boolean | 否 | 粗体 |
| HTextAlign | String | 否 | "Center" / "Left" / "Right"，默认 "Center" |
| IsReadOnly | Boolean | 否 | 运行时不可更改（状态显示用） |
| Margin | Integer | 否 | 边距，默认 0 |
| Padding | Integer | 否 | 控件图形内边距，默认 1 |
| PrettyName | String | 否 | 控件引脚别名，用 "~" 创建子层级 |
| Radius | Integer | 否 | 同 CornerRadius |
| StrokeColor | Table | 否 | 边框颜色 `{r,g,b,alpha}`，默认黑 |
| StrokeWidth | Integer | 否 | 边框宽度，默认 1 |
| VTextAlign | String | 否 | "Center" / "Top" / "Bottom"，默认 "Center" |
| ZOrder | Signed Integer | 否 | 垂直平面位置，范围 -2147483648 到 2147483647 |

#### Button-Only Properties

| 属性 | 类型 | 必填 | 说明 |
|------|------|------|------|
| ButtonStyle | String | 是 | "Toggle" / "Momentary" / "Trigger" / "StateTrigger" / "On" / "Off" / "Custom"（string 类型按钮用 "Custom"） |
| ButtonVisualStyle | String | 否 | "Flat" / "Gloss"，默认 "Gloss" |
| CornerRadius | Integer | 否 | 圆角半径 |
| CustomButtonUp | String | 否 | Custom 按钮抬起时显示的字符串 |
| CustomButtonDown | String | 否 | Custom 按钮按下时显示的字符串 |
| Legend | String | 否 | 按钮图例 |
| OffColor | Table | 否 | UnlinkOffColor=true 时按钮关闭颜色 |
| UnlinkOffColor | Boolean | 否 | 允许按钮显示完全不同的开/关颜色 |
| IconColor | Table | 否 | 按钮图标颜色 |
| WordWrap | Boolean | 否 | 图例文本是否换行 |

> **Note**: "Off"、"On"、"Custom" 选项等同于 Q-SYS Help 中的 "Off"、"On"、"String" push-actions。

#### Fader-Only Properties

| 属性 | 类型 | 必填 | 说明 |
|------|------|------|------|
| ShowTextbox | Boolean | 否 | 显示当前值文本框，默认 false |

#### Meter-Only Properties

| 属性 | 类型 | 必填 | 说明 |
|------|------|------|------|
| CornerRadius | Integer | 否 | 圆角 |
| BackgroundColor | Table | 否 | 仪表背景色 |
| MeterStyle | String | 是 | "Level" / "Reduction" / "Gain" / "Standard" |
| ShowTextbox | Boolean | 否 | 显示值文本框，默认 true |

#### Text-Only Properties

| 属性 | 类型 | 必填 | 说明 |
|------|------|------|------|
| CornerRadius | Integer | 否 | 圆角 |
| TextBoxStyle | String | 否 | "Normal" / "Meter" / "NoBackground"，默认 "Normal" |
| WordWrap | Boolean | 否 | 图例文本换行 |

```lua
function GetControlLayout(props)
  local layout = {}
  local graphics = {}

  layout["TextBox"]={
    Style="Text",
    IsReadOnly=true,
    Position={0,0},
    Size={100,16},
    TextColor={255,255,255},
    TextBoxStyle="NoBackground",
    FontSize=9,
    HTextAlign="Left",
    VTextAlign="Center",
    Font = "Montserrat",
    FontStyle = "SemiBold",
  }

  -- 多个 LED 指示器
  for idx = 1,5 do
    layout["LEDIndicator "..idx]={
      PrettyName="LED-State",
      Style="LED",
      Color={0,255,0},
      OffColor={0,0,0},
      UnlinkOffColor=true,
      Position={0,28},
      Size={16,16},
      CornerRadius=8
    }
  end

  -- 插件背景
  table.insert(graphics,{
    Type="GroupBox",
    Position={0,0},
    Size={200,200},
    Fill={0,0,0},
    CornerRadius=0,
    StrokeColor={0,0,0},
    StrokeWidth=1
  })

  -- 标签
  table.insert(graphics,{
    Type="Label",
    Text="This is a label",
    Position={0,40},
    Size={100,14},
    Color={255,255,255},
    FontSize=9,
    HTextAlign="Left"
  })

  return layout,graphics
end
```

---

### 8. Graphics Table Properties（图形表属性）

| 属性 | 类型 | 必填 | 说明 |
|------|------|------|------|
| Position | Table | 是 | 位置 `{x,y}` |
| Size | Table | 是 | 尺寸 `{x,y}` |
| Type | String | 是 | "Label"（固定文本）/ "GroupBox"（带标题的外框）/ "Header"（单线条标题）/ "Image"（图片，非SVG）/ "Svg"（SVG图片） |
| ZOrder | Signed Integer | 否 | 垂直平面位置 |

#### GroupBox-Only Properties

| 属性 | 类型 | 说明 |
|------|------|------|
| CornerRadius | Integer | 圆角 |
| Text | String | 标题文本（默认无） |
| Font | String | 默认 "Roboto" |
| FontSize | Integer | 字号 |
| FontStyle | FontStyle | 字体样式 |
| IsBold | Boolean | 粗体 |
| HTextAlign | String | "Center"/"Left"/"Right"，默认 "Center" |
| StrokeWidth | Integer | 边框宽度 0-64，默认 0 |
| StrokeColor | Table | 边框颜色，默认黑 |
| Color | Table | 文本颜色 |
| Fill | Table | 填充色，默认透明 |

#### Header-Only Properties

| 属性 | 类型 | 说明 |
|------|------|------|
| Text | String | 标题文本 |
| Font / FontSize / FontStyle / IsBold / HTextAlign / Color | 同 GroupBox |

#### Image/SVG-Only Properties

| 属性 | 类型 | 必填 | 说明 |
|------|------|------|------|
| Image | String | 是 | Base64 编码的 JPG/PNG/SVG 字符串 |

#### Label-Only Properties

| 属性 | 类型 | 说明 |
|------|------|------|
| Color | Table | 标签颜色 |
| CornerRadius | Integer | 圆角 |
| Margin | Integer | 边距，默认 0 |
| Padding | Integer | 文本边框内边距，默认 1 |
| Text / Font / Fill / FontSize / FontStyle / IsBold / HTextAlign / VTextAlign / StrokeWidth / StrokeColor | 文本相关 |

---

### 9. Object Layering（对象层级 / ZOrder）

QDS 通常自动处理控件和图形的叠加（z-order）。可通过 `ZOrder` 手动设置对象在垂直平面的位置，值越大越靠前。ZOrder 同时适用于图形元素和控件（它们在同一层级方案中）。

> **Note**: 如果对任一控件或图形使用了 ZOrder，建议对所有控件和图形都使用，否则可能出现奇怪效果。

---

### 10. Using Multiple Pages（多页面使用）

多页面插件的控件布局需分两部分：
1. 所有页面通用的控件和图形
2. 仅在特定页面显示的控件和图形

通用控件正常添加。特定页面的控件需加条件判断，可使用页面的数字索引或页面名称：

```lua
-- 方式1：使用页面索引
if props['page_index'].Value == 1 then
  -- 第一页的控件
elseif props['page_index'].Value == 2 then
  -- 第二页的控件
end

-- 方式2：使用页面名称
local CurrentPage = pagenames[props["page_index"].Value]
if CurrentPage == "Page 1" then
  -- 第一页的控件
elseif CurrentPage == "Page 2" then
  -- 第二页的控件
end
```

> **Tip**: 多页面插件的典型用例是根据属性值改变页面显示。默认页面用数组定义，在 GetProperties() 中可根据属性设置添加额外页面。但 GetControls() 或 GetControlLayout() 被调用时，页面名称数组会恢复为默认页面。GetProperties() 中的修改不会传递。因此需要创建单独的 helper 函数，根据属性从头创建完整页面名称数组，并在 GetControls()/GetControlLayout() 中调用。

---

### 11. GetComponents(props) — 可选

在插件中嵌入一个或多个音频组件以进行音频处理。返回组件表。嵌入的组件在插件 UI 中不可见，所需控件必须手动添加到 UI。事件处理函数用于更新嵌入组件控件。音频信号使用 GetPins() 添加音频引脚，GetWiring() 连线。

| 属性 | 类型 | 必填 | 说明 |
|------|------|------|------|
| Name | String | 是 | 组件名称（不能含空格） |
| Type | String | 是 | 组件类型，如 'mixer', 'scriptable_controls' 等 |
| Properties | Table | 是 | 组件属性值，如输入/输出通道数 |

> **Note**: 嵌入组件会增加设计的通道数和组件数。某些组件有限制（如 Audio Player 最多 32 通道，Audio Recorder 仅 1 个组件 4 通道）。超出限制会导致编译失败，且用户看不到原因。这种情况考虑用 Named Component 代替。

```lua
function GetComponents(props)
  local components = {}
  table.insert(components,{
    Name = "Mixer",
    Type = "mixer",
    Properties = {
      ["n_inputs"] = 8,
      ["n_outputs"] = 1,
    }
  })
  table.insert(components, {
    Name = "SignalPresence",
    Type = "signal_presence",
    Properties = { ["multi_channel_type"] = 1 }
  })
  return comp
end
```

---

### 12. GetPins(props) — 可选

为插件对象添加音频或串行引脚。控件引脚不在此定义（在 GetControls 的 UserPin/PinStyle 中定义）。

| 属性 | 类型 | 必填 | 说明 |
|------|------|------|------|
| Name | String | 是 | 引脚名称 |
| Direction | String | 是 | "input" / "output" |
| Domain | String | 否 | 引脚类型，默认音频。设为 "serial" 为串行引脚 |

> **Note**: 此函数只能添加音频或串行引脚。

```lua
function GetPins(props)
  local pins = {}
  table.insert(pins,{
    Name = "Audio Input",
    Direction = "input"
  })
  table.insert(pins,{
    Name = "Audio Output",
    Direction = "output"
  })
  return pins
end
```

---

### 13. GetWiring(props) — 可选

返回描述组件与插件引脚之间连线的对象表。每个连线对象是字符串表，定义源和一个或多个目标。

> **Note**: 如果嵌入音频组件的所有输入输出引脚都在 GetWiring() 中引用了，音频不会通过。

#### 引脚连线规则

- 插件输入引脚可连接到组件输入引脚或插件输出引脚
- 插件输入引脚可连接到多个组件输入引脚
- 组件输入引脚只能连接到单个插件输入引脚
- 组件输出引脚可连接到多个插件输出引脚
- 插件输出引脚只能连接到单个组件输出引脚

```lua
function GetWiring(props)
  local wiring = {}
  -- 插件输入引脚 "In 1" → 嵌入组件输入引脚 1
  table.insert(wiring,{
    "In 1",
    "main_mixer Input 1"
  })
  -- 嵌入组件输出引脚 1 → 插件输出引脚 "Mix Output"
  table.insert(wiring,{
    "main_mixer Output 1",
    "Mix Output"
  })
  -- 引用未使用的引脚以允许内部音频流入嵌入组件
  table.insert(wiring,{
    "main_mixer Output 2"
  })
  -- 插件输入引脚连接到多个嵌入组件输入引脚
  table.insert(wiring,{
    "In 2",
    "main_mixer Input 2",
    "meter Input"
  })
  return wiring
end
```

> **Tip**: 在 QDS 中可用 Tools > View Component Controls Info 查看组件的控制引脚名称。

---

## 二、运行时 / Run-time

### Properties（运行时属性访问）

运行时通过全局 `Properties` 表访问属性当前值，以属性名为键，读 `.Value`：

```lua
myValue = Properties["Property Name"].Value  -- 所有类型通用
```

### Controls（运行时控件访问）

与 Text Controller 一样，全局 `Controls` 表包含所有插件控件。Count > 1 时为 1-indexed 数组。

```lua
-- Count = 1
local level = .8  -- 80%
Controls["Zone Level"].Value = level

-- Count > 1
local zone = 2
local level = .8  -- 80%
Controls["Zone Level"][zone].Value = level

-- 别名
myControlAlias = Controls["MyControlName"]       -- 方括号
myOtherControlAlias = Controls.MyOtherControlName  -- 点号（等效）
```

### Components（运行时嵌入组件访问）

通过 GetComponents 添加的组件在运行时可通过分配的名称访问：

```lua
if Controls then
  function Init()
    print("v"..PluginInfo.BuildVersion)
    Controls.mute.Boolean = GainRamp["to.b"].Boolean
    GainRamp["time.a"].Value = Controls.OnTime.Value
    GainRamp["time.b"].Value = Controls.OffTime.Value
    GainRamp["release"].Value = .1
    GainRamp["gain.a"].Value = 0
    GainRamp["gain.b"].Value = -100
  end
  Init()
end
```

---

## 三、推荐函数 / Recommended Functions（非保留，QSC 官方插件常用模式）

这些函数不是必须的，但常见于 QSC 官方插件，用于提高代码可读性和一致性。参考 TCPSocket.qplug 示例。

| 函数 | 说明 |
|------|------|
| SetupDebugPrint() | 根据 Debug Print 属性设置标志，控制打印到调试窗口的消息 |
| Send(cmd) | 通过 socket 发送数据 |
| ClearVariables() | 连接中断或重置时清空控件、变量、表和标志 |
| Connect() | 连接建立后设置标志或触发其他函数 |
| Disconnected() | 连接中断时重置标志或触发其他函数 |
| GetDeviceInfo() | 与设备的初始数据交换（如请求序列号等静态数据） |
| PollDevice() | 定期请求需要轮询变化的数据，维护连接健康 |
| ParseResponse() | 处理 socket 接收的数据，确定上下文并分发到具体处理函数 |
| Initialization() | 插件启动时调用一次，初始化需要设置的部分 |

---

## 四、字体和 FontStyle 组合 / Font and FontStyle Combinations

> **Note**: FontStyle 大小写因字体而异。

| Font | FontStyle 选项 |
|------|---------------|
| Adamina | Regular |
| Droid Sans | Regular, Bold |
| Lato | Light, Light Italic, Regular, Italic, Bold, Bold Italic, Black, Black Italic |
| Montserrat | Thin, Thin Italic, ExtraLight, ExtraLight Italic, Light, Light Italic, Regular, Italic, Medium, Medium Italic, SemiBold, SemiBold Italic, Bold, Bold Italic, ExtraBold, ExtraBold Italic, Black, Black Italic |
| Noto Serif | Regular, Italic, Bold, BoldItalic |
| Open Sans | Light, Light Italic, Regular, Italic, Semibold, Semibold Italic, Bold, Bold Italic, Extrabold, Extrabold Italic |
| Poppins | Light, Regular, Medium, SemiBold, Bold |
| Roboto | Thin, Thin Italic, Light, Light Italic, Regular, Italic, Medium, Medium Italic, Bold, Bold Italic, Black, Black Italic |
| Roboto Mono | Thin, Thin Italic, Light, Light Italic, Regular, Italic, Medium, Medium Italic, Bold, Bold Italic |
| Roboto Slab | Thin, Light, Regular, Bold |
| Slabo 27px | Regular |
