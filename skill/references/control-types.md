# 控件类型速查

## Button（按钮）

```lua
{
  Name = "MyButton",
  ControlType = "Button",
  ButtonType = "Toggle",    -- Toggle | Momentary | Trigger
  DefaultValue = false,
  PinStyle = "Input",       -- Input | Output
  UserPin = true,
  Count = 1
}
```

| ButtonType | 行为 |
|------------|------|
| Toggle | 点击切换 true/false，保持状态 |
| Momentary | 按下 true，松开 false |
| Trigger | 点击瞬间 true，自动复位 |

**运行时**：`Controls.MyButton.Boolean` (true/false)

## Knob（旋钮/滑条）

```lua
{
  Name = "MyKnob",
  ControlType = "Knob",
  ControlUnit = "Integer",  -- REQUIRED for external pins!
  Min = 0,
  Max = 65535,
  DefaultValue = 0,
  PinStyle = "Input",
  UserPin = true,
  Count = 1
}
```

**运行时**：`Controls.MyKnob.Value` (number)

**重要**：必须设置 `ControlUnit = "Integer"`，否则外部引脚不显示。

## Text（文本）

```lua
{
  Name = "MyText",
  ControlType = "Text",
  DefaultValue = "",
  PinStyle = "Output",      -- 可选
  UserPin = true,           -- 可选
  Count = 1
}
```

**运行时**：`Controls.MyText.String` (string)

**用途**：状态显示、日志输出、数值显示。Output 引脚可作为文本信号输出。

## Indicator（指示灯）

```lua
{
  Name = "MyLed",
  ControlType = "Indicator",
  DefaultValue = false,
  PinStyle = "Output",
  UserPin = true,
  Count = 1
}
```

**运行时**：`Controls.MyLed.Boolean` (true/false)

## 动态数量控件

```lua
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
end
```

**运行时访问**：`Controls["Digital_In_" .. i]`

## 面板布局中的控件样式

```lua
layout["MyButton"] = {
  PrettyName = "My Button",
  Legend = "Enable",
  Style = "Button",
  ButtonStyle = "Toggle",   -- Toggle | Momentary
  Position = {20, 40},
  Size = {100, 30}
}

layout["MyKnob"] = {
  PrettyName = "Value",
  Legend = "Level",
  Style = "Knob",
  Position = {20, 80},
  Size = {60, 30}           -- 小尺寸避免巨大圆形
}

layout["MyText"] = {
  PrettyName = "Status",
  Style = "Text",
  Position = {20, 120},
  Size = {200, 20}
}
```

## 静态图形（graphics）

### GroupBox
```lua
{
  Type = "GroupBox",
  Text = "Status",
  FontSize = 12,
  Position = {8, 8},
  Size = {324, 200}
}
```

### Text（静态文字）
```lua
{
  Type = "Text",
  Text = "Hello World",
  FontSize = 11,
  Position = {20, 40},
  Size = {200, 20}
}
```

### Line
```lua
{
  Type = "Line",
  Position = {8, 100},
  Size = {324, 0}
}
```

## 控件引脚方向速查

| PinStyle | UserPin | 结果 |
|----------|---------|------|
| "Input" | true | 输入引脚，外部可连接 |
| "Output" | true | 输出引脚，外部可连接 |
| "Input" | false | 仅面板使用，无引脚（但可能仍显示！） |
| 不写 | false | 仅面板使用，无引脚（推荐方式） |

**规则**：不需要外部引脚的控件，完全不写 PinStyle。
