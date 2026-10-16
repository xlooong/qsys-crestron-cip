# Plugin Evaluation Script

> 来源: https://github.com/Q-SYS-Communities-for-Developers/Plugin-Evaluation-Script
> 用途: 评估 .qplug 文件的设计时合规性，检查语法错误和 SDK 标准符合性

## Overview

Q-SYS Plugin 开发者可以使用此工具评估 .qplug 文件的设计时合规性，发现语法错误，确保符合 SDK 标准。

### 评估内容

- 检查 PluginInfo 表中的必需和可选信息
- 检查保留控件名（鼓励在适当时候使用）
- 检查 Properties、Controls、graphics、layout 项的正确键和允许值
- 生成 JSON 输出，可用于其他工具和自动化
- 将报告分为 errors、warnings、notices

## Setup and Requirements

- 安装 JQ: https://jqlang.github.io/jq/download/
  - GitHub hosted runners 已预装
- 在 Windows 11 的 GitBash 终端测试
- 捆绑了 lua 5.3 可执行文件和 json.lua

## Usage

```bash
./EvaluatePlugin.sh Path_to_file [-maxprops] [prop=value]
```

- `-maxprops`: 将所有 boolean 设为 true，integer/double 设为最大值
- 属性名中的空格用 `%20` 代替

### 示例

```bash
./EvaluatePlugin.sh ./test.qplug
./EvaluatePlugin.sh ./test.qplug -maxprops
./EvaluatePlugin.sh ./test.qplug Inputs=7 Poll%20Rate=10
./EvaluatePlugin.sh C:\Users\John.Doe\Documents\Temp\test.qplug
```

## PluginEvalConfig.json

### Settings

- **VarsToReset**: 在每次调用保留函数之前重置为初始状态的变量列表

### Exceptions

- **KeyValues**: 用于忽略 GetControls 和 GetControlLayout 中的非 SDK 键值对
  - `type`: "ControlKey" 或 "LayoutKey"
  - `value`: 要忽略的键名
- **PrettyNamelessControls**: 不警告缺少 PrettyName 定义的控件名列表
- **PinlessControls**: 不警告缺少控件引脚定义的控件名列表
- **AllowSpacesInControlNames**: 如果为 true，不警告控件名中包含空格

### 示例

```json
{
  "Settings": {
    "VarsToReset": []
  },
  "Exceptions": {
    "KeyValues": [
      { "type": "ControlKey", "value": "IsShared" }
    ],
    "PrettyNamelessControls": [],
    "PinlessControls": [],
    "AllowSpacesInControlNames": false
  }
}
```

## Outputs

### /output/PluginJson.json

所有控件、图形、属性、引脚、页面、错误、通知、警告和信息的 JSON 表示。

### /output/PluginReport.json

仅包含 Notices、Warnings 和 Errors 的 JSON。

## SDK 标准（从 evaluateDesignTime.lua 提取）

### PluginInfo 必需字段

| 字段 | 要求 | 说明 |
|------|------|------|
| Id | **必需** | 唯一插件 ID |
| Author | **必需** | 作者 |
| Name | **必需** | 插件名称 |
| Version | **必需** | 版本号，格式 x.x / x.x.x / x.x.x.x |
| Manufacturer | 警告 | 制造商 |
| BuildVersion | 通知 | 不被 Designer 读取，应使用 Version |

### Property 类型

- `string`, `integer`, `double`, `boolean`, `enum`

### Property 键

`Name`, `Type`, `Header`, `Value`, `Min`, `Max`, `Choices`, `Comment`, `Description`, `_index`

### Property 校验规则

- integer/double 类型必须有 Min 和 Max
- Min 必须小于等于 Max
- Value 必须在 Min/Max 范围内
- enum 类型必须有 Choices，且 Value 必须在 Choices 中
- boolean 类型 Value 必须是 boolean
- integer 类型 Value 必须是 number

### 保留属性名（禁止使用）

`ismanaged`, `is managed`, `isrequired`, `is required`, `location`, `showdebug`, `show debug`, `page_index`, `name`, `script access`, `code name`, `internal_designator`

### Control 类型

`Button`, `Knob`, `Indicator`, `Text`

### Control 键

`Name`, `Count`, `ControlType`, `PinStyle`, `UserPin`, `ButtonType`, `ControlUnit`, `IndicatorType`, `DefaultValue`, `Icon`, `IconType`, `Min`, `Max`, `Description`

### PinStyle 值

`Input`, `Output`, `Both`, `None`

### ButtonType 值

`Momentary`, `Toggle`, `Trigger`, `StateTrigger`, `On`, `Off`, `Custom`

### ControlUnit 值

`dB`, `Hz`, `Float`, `Integer`, `Pan`, `Percent`, `Position`, `Seconds`

### IndicatorType 值

`Led`, `Meter`, `Text`, `Status`, `StatusGP`

### 保留控件名（鼓励使用）

`Status`, `IPAddress`, `MACAddress`, `Username`, `Password`, `DeviceName`, `DeviceFirmware`, `SerialNumber`

### Layout 键

`Style`, `Position`, `Size`, `Color`, `TextColor`, `ClassName`, `Font`, `FontSize`, `TextFontSize`, `FontStyle`, `HTextAlign`, `VTextAlign`, `IsReadOnly`, `Margin`, `Padding`, `PrettyName`, `Radius`, `StrokeColor`, `StrokeWidth`, `ZOrder`, `IconColor`

### Button Layout 键

`ButtonStyle`, `ButtonVisualStyle`, `CornerRadius`, `CustomButtonUp`, `CustomButtonDown`, `Legend`, `OffColor`, `UnlinkOffColor`, `WordWrap`, `IsBold`

### Fader Layout 键

`ShowTextbox`

### Meter Layout 键

`BackgroundColor`, `MeterStyle`, `ShowTextbox`

### MeterStyle 值

`Level`, `Reduction`, `Gain`, `Standard`

### Text Layout 键

`CornerRadius`, `TextBoxStyle`, `WordWrap`, `IsBold`

### Led Layout 键

`OffColor`, `UnlinkOffColor`

### Layout ControlStyle 值

`Fader`, `Knob`, `Button`, `Text`, `Meter`, `Led`, `ListBox`, `ComboBox`, `Html`, `Media`, `None`

## 常见检查项

### Errors（错误）

- PluginInfo.Id/Author/Name/Version 未设置
- Version 格式不正确
- Property 缺少 Name/Type/Value
- Property Type 不被识别
- enum 类型缺少 Choices 或 Value 不在 Choices 中
- integer/double 缺少 Min/Max 或 Min > Max
- Property 名与保留属性冲突
- Control 缺少 ControlType 或 ControlType 不被识别
- Control 缺少 PinStyle
- Control 在 Layout 中没有定义
- Layout 中引用了不存在的 Control
- Code Pin 出现在 Layout 中

### Warnings（警告）

- PluginInfo.Manufacturer 未设置
- Control 键不被识别
- Property 键不被识别
- Control 名中包含句号（.）
- Control 名中包含空格（可配置忽略）

### Notices（通知）

- PluginInfo.BuildVersion 已设置（应使用 Version）
- GetPages() 未定义（默认为单页插件）
- 找到保留控件名
- Status Control 未找到
- Control 缺少 PrettyName
- Control PinStyle 设为 None

## Known Issues

- 设计时有 print 语句会导致脚本失败
- 脚本不会像 Designer 那样为每个保留函数调用关闭并重新运行 lua。如果全局变量在保留函数中被修改，可能需要将其添加到 PluginEvalConfig.json 的 Settings.VarsToReset 中

## Support

所有支持问题、bug 报告和功能请求应在 GitHub 仓库提交 issues，不要直接联系 QSC Support。
