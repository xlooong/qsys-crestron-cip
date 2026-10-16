# Locimation qsys-plugins 学习笔记

> 来源: https://github.com/locimation/qsys-plugins
> 90 stars, 16 forks, MIT License
> 作者: Michael Goodyear (Locimation Pty Ltd)
> 学习时间: 2026-10-12

## 仓库结构

按设备/功能分类的插件集合：
- **Logic** — Match, Stepper, FSM（有限状态机）
- **Blackmagic** — 设备控制
- **DMX** — DMX 控制
- **Dolby** — 杜比设备
- **MA2** — 灯光控台
- **NEC/Series 2 Cinema** — 投影机
- **Network Monitor** — Link Monitor, MAC Monitor (SNMP)
- **SVSi** — 视频分发
- **Shure** — 无线话筒
- **WebStream** — 网络流

## 代码模式与最佳实践

### 1. PluginInfo 标准格式

```lua
PluginInfo = {
  Name = 'Locimation~Match',           -- 厂商~插件名
  Description = "Initial release",
  Version = "1.0.0",                    -- 语义化版本
  Id = "61e8a3e7-a055-449c-83c4-302d7d33e83b",  -- UUID
  ShowDebug = false
}
```

**关键点**:
- `Id` 使用 UUID，确保全局唯一
- `Name` 用 `厂商~插件名` 格式
- `Version` 语义化，Q-SYS 靠版本号判断更新

### 2. GetPrettyName 动态组件名

```lua
function GetPrettyName(props)
  return (props['Match Count'].Value > 1) and 'Multi-match' or 'Match';
end
```

根据属性动态显示组件名称，用户在设计图上能直接看到配置状态。

### 3. GetColor 自定义组件颜色

```lua
function GetColor()
    return { 70, 110, 240 };  -- RGB
end
```

### 4. RectifyProperties 动态属性控制

```lua
function RectifyProperties(props)
    props["Allow Looping"].IsHidden = (props["Direction"].Value ~= "Sequential");
    return props;
end
```

根据其他属性值动态隐藏/显示属性，避免无效配置。

### 5. 多计数控件的命名约定

当 Count > 1 时，控件自动命名为 `Name 1`, `Name 2`...
当 Count == 1 时，控件名就是 `Name`（无序号）。

```lua
local function n(p, i)
  if(props['Match Count'].Value == 1) then
    return p;
  else
    return ('%s %d'):format(p, i);
  end;
end;
```

布局中也用同样的逻辑：
```lua
if(props['Steps'].Value == 1) then
  controls['Delay'] = dStyle;
else
  controls['Delay ' .. i] = dStyle;
end;
```

### 6. Ctls 表统一访问模式

```lua
Ctls = {};
for n,c in pairs(Controls) do
  Ctls[n] = (type(c) == 'table') and c or {c};
end;
```

将所有控件统一转为数组（即使 Count=1 也包成 `{c}`），这样遍历时不需要判断单/多。

### 7. Trigger 按钮处理

```lua
{
  Name = "Trigger",
  ControlType = "Button",
  ButtonType = "Trigger",
  UserPin = false,
  PinStyle = 'Both'
}
```

Trigger 按钮的 EventHandler 中不需要判断 `c.Boolean`，直接执行。

### 8. Stepper 的定时器驱动模式

用固定 tick 定时器 + 时间累加器实现步进序列：

```lua
TICK = 0.01;  -- 10ms 精度
TIME = math.maxinteger;  -- 用 maxinteger 表示"未运行"
T = Timer.New();
T.EventHandler = function()
  local sTime, eTime = 0,0;
  for i,c in pairs(Ctls.Output) do
    sTime = eTime + Ctls.Delay[i].Value;
    eTime = sTime + Ctls.Length[i].Value;
    Ctls.Output[i].Boolean = (TIME >= sTime and TIME < eTime);
  end;
  Controls.Busy.Boolean = (TIME <= eTime);
  Controls.Bar.Position = (TIME ~= math.maxinteger) and (TIME / eTime) or 0;
  if(TIME <= eTime) then
    TIME = TIME + TICK;
  else
    TIME = math.maxinteger;  -- 结束
  end;
end;
T:Start(TICK);

Controls['Trigger'].EventHandler = function()
  TIME = 0;  -- 开始
end;
Controls['Reset'].EventHandler = function()
  TIME = math.maxinteger;  -- 重置
end;
```

**优点**: 单一定时器驱动所有步进，时间精度高，支持进度条输出。

### 9. FSM 的 LOCKOUT 防重入

```lua
LOCKOUT = true;
Timer.CallAfter(function()
    Controls["Current State"].Value = i;
    updateLeds(i);
    LOCKOUT = false;
end, 0);
```

用 `Timer.CallAfter(..., 0)` 延迟到下一帧执行状态切换，配合 LOCKOUT 防止快速连续触发导致状态混乱。

### 10. 布局中的 PrettyName 分组

```lua
controls["Active " .. i] = {
  Position = {0, i * 16 },
  PrettyName = string.format("State %d~Active", i)
};
```

`PrettyName` 用 `分组~名称` 格式，在控件树中自动分组显示。

### 11. ComboBox 控件

```lua
{
  Name = 'Type',
  ControlType = 'Text',
  Count = props['Match Count'].Value,
  UserPin = true,
  PinStyle = 'Both'
}
-- 布局中
controls[n('Type', i)] = {
  Style = 'ComboBox',
  Position = { 166, 60 + i * 20 },
  Size = { 100, 20 },
};
-- 运行时设置选项
for _,c in ipairs(Ctls.Type) do
  c.Choices = {'Exact', 'Pattern'};
  if(c.String == '') then c.String = 'Exact'; end;
end;
```

Text 控件 + `Style = 'ComboBox'` + 运行时设置 `.Choices` 实现下拉框。

### 12. LED 颜色控制

```lua
controls[n('Matches', i)] = {
  Style = 'Button',
  Color = { 0, 255, 0 },        -- ON 颜色 (RGB table)
  UnlinkOffColor = true,         -- 允许独立 OFF 颜色
  OffColor = { 124, 0, 0 },      -- OFF 颜色
  Legend = 'NO',
};
-- 运行时
Ctls.Matches[i].Boolean = matches;
Ctls.Matches[i].Legend = (matches and 'YES' or 'NO');
```

Indicator LED 用 `Style = 'Button'`，支持独立 ON/OFF 颜色。

### 13. SVG Logo 嵌入

```lua
LOGO = [[PD94bWwg...base64 encoded SVG...]];
-- 布局 graphics 中
{
  Type = "Svg",
  Position = { 4, 100 },
  Size = { 150, 100 },
  Image = LOGO
}
```

Base64 编码的 SVG 直接嵌入源码，在面板中显示品牌 Logo。

### 14. 许可证头

每个文件开头都有完整的 MIT 许可证注释块，这是开源项目的标准做法。

## 与我们 wxl_personal_plug 的对比

| 方面 | Locimation | 我们的 | 改进建议 |
|------|-----------|--------|---------|
| PluginInfo.Id | UUID | 未使用 | **应加 UUID**，避免与其他插件冲突 |
| 版本号 | 语义化 1.0.0 | 已遵守 | 保持 |
| Ctls 统一数组 | ✅ | 部分使用 | **全部统一**，简化遍历逻辑 |
| GetPrettyName | ✅ 动态 | 未使用 | 可加入，提升设计图可读性 |
| RectifyProperties | ✅ 动态隐藏 | 未使用 | 可加入，避免无效属性 |
| PrettyName 分组 | `State 1~Active` | 未使用 | **应加入**，控件树更清晰 |
| ComboBox | Text+Style | 未使用 | 可用于模式选择 |
| 定时器驱动步进 | 10ms tick + 累加器 | Timer.CallAfter 嵌套 | 复杂序列可参考 |
| LOCKOUT 防重入 | ✅ | 部分使用 | 状态切换类插件应加入 |
| SVG Logo | ✅ | 未使用 | 可加入品牌标识 |
| 许可证 | MIT 头 | 无 | 开源时需加 |

## 可直接复用的模式

1. **Ctls 统一数组** — 所有控件转数组，遍历不用判断单/多
2. **n(p, i) 命名函数** — 自动处理 Count=1 时无序号的情况
3. **LOCKOUT + Timer.CallAfter(0)** — 状态切换防重入
4. **Stepper 时间累加器** — 用 `math.maxinteger` 表示空闲，TIME=0 表示开始
5. **ComboBox 下拉框** — Text 控件 + Style='ComboBox' + .Choices
6. **PrettyName 分组** — `分组~名称` 格式
