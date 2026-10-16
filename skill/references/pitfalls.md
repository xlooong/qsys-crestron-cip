# qplug 开发踩坑记录

## 致命错误（导致插件无法加载）

### 1. GetAllControlPanels: <name> not defined
**症状**：拖入插件时报错，整个分类消失
**根因**：`GetPages` 返回了字符串数组而非表数组
```lua
-- 错误
return {"Main", "Settings"}
-- 正确
return { {name = "Main"}, {name = "Settings"} }
```

### 2. get_Properties: function 'GetProperties' not defined
**症状**：插件加载报错
**根因**：用了 `Properties = {...}` 表而非 `GetProperties()` 函数
```lua
-- 错误
Properties = { {Name = "x", ...} }
-- 正确
function GetProperties()
  return { {Name = "x", ...} }
end
```

### 3. unexpected symbol near ')'
**症状**：插件加载报错，行号指向末尾
**根因**：括号不匹配或语法错误。用 Python 检查括号配对。

### 4. 语法错误导致整个分类消失
**症状**：wxl_personal_plug 文件夹在 Designer 中消失
**根因**：任一 qplug 有语法错误，Q-SYS 会跳过整个分类
**解决**：修复语法错误后重启 Designer

## 引脚不显示问题

### 5. Knob 控件不显示外部引脚
**症状**：Digital/Serial 引脚正常，Analog(Knob) 引脚缺失
**根因**：Knob 控件缺少 `ControlUnit = "Integer"`
```lua
-- 错误（无引脚）
{ Name = "Analog_1", ControlType = "Knob", PinStyle = "Output", UserPin = true }
-- 正确（有引脚）
{ Name = "Analog_1", ControlType = "Knob", ControlUnit = "Integer",
  PinStyle = "Output", UserPin = true }
```

### 6. UserPin=false 的控件仍出现在引脚列表
**症状**：设置了 UserPin=false，但引脚列表中仍有该控件
**根因**：同时设置了 `PinStyle` 属性。PinStyle 优先级高于 UserPin
**解决**：不需要引脚的控件**完全不写 PinStyle**

### 7. Text 控件 Output 引脚不显示
**症状**：Text 控件设了 PinStyle="Output" UserPin=true，但引脚不出现
**根因**：Q-SYS Text 类型 Output 引脚可能需要 DefaultValue 为空字符串
**解决**：设 `DefaultValue = ""`，确保控件在静态区定义（不在动态循环后）

## 面板布局问题

### 8. Notes 超框
**症状**：面板底部 Notes 文字被截断
**根因**：GroupBox 高度不够
**解决**：GroupBox 高度 = 起始Y + 行数×13 + 30px 边距。42 行 Notes 需要约 580px 高。

### 9. 控件超框
**症状**：按钮/文字超出面板边界
**根因**：坐标计算错误或面板尺寸不够
**解决**：所有元素留 8-15px 边距，GroupBox 比内容大 20-30px

### 10. Knob 太大
**症状**：面板上 Knob 显示为巨大的圆形
**根因**：Knob 默认尺寸较大
**解决**：layout 中设置较小的 Size，如 {60, 30}

## 运行时问题

### 11. os.clock() 不可靠
**症状**：watchdog 超时检测不工作，时间不递增
**根因**：Q-SYS Core 上 os.clock() 返回 CPU 时间，非墙上时钟
**解决**：用 `os.time()` 代替

### 12. Timer.IsRunning 报错
**症状**：`timer.IsRunning` 返回 nil 或报错
**根因**：IsRunning 是方法不是属性
**解决**：用 `timer:IsRunning()`

### 13. TCP 假连接不自动重连
**症状**：Crestron 重启后，Connected 灯亮但无通讯，需手动断开重连
**根因**：TCP 连接未正常关闭，Q-SYS 认为连接还在
**解决**：添加两级 watchdog：
- Level 1：20 秒无任何 TCP 数据 → 强制重连
- Level 2：注册后 15 秒无信号数据 → 强制重连

### 14. Trigger 脉冲太短 Crestron 收不到
**症状**：Digital 输出接 Trigger，偶尔不触发
**根因**：Trigger 瞬间 true→false，CIP 包间隔仅几毫秒
**解决**：添加 digital_pulse_width 属性（默认 0.3s），拉伸脉冲

### 15. Toggle 按钮太灵敏
**症状**：点一下数字变好几次
**根因**：按钮事件重复触发
**解决**：EventHandler 中立即 `c.Boolean = false` 复位，或加防抖

## CIP 协议问题

### 16. 注册后无初始数据
**症状**：CIP 注册成功，但 Crestron 不发送初始 join 值
**根因**：注册后需发送更新请求包
```lua
tcp:Write(string.char(0x05,0x00,0x05,0x00,0x00,0x02,0x03,0x00))
```

### 17. 0x03 断开包处理
**症状**：Crestron 程序停止后不自动重连
**根因**：0x03 处理中调用了 doDisconnect()，设置了 userDisconnected=true
**解决**：0x03 是对端主动断开，不是用户断开。内联清理，保持 userDisconnected=false

### 18. 心跳不回复
**症状**：连接后 Crestron 断开
**根因**：收到 0x0D 心跳请求未回复 0x0E
**解决**：收到 0x0D 立即发送 `string.char(0x0E,0x00,0x02,0x00,0x00)`

### 19. 运行时属性值获取错误（致命）
**症状**：面板渲染正常但按钮不能按、Status 文字空白、调试窗口无启动日志
**根因**：运行时用 `Properties.name` 获取属性，返回的是属性对象而非数值。对象与数字比较/拼接导致 Lua 报错，初始化中断，EventHandler 无法绑定
**解决**：运行时必须用 `tonumber(Properties["name"].Value) or 默认值`
```lua
-- 错误（返回对象，运行时报错）
local pw = Properties.pulse_width
-- 正确（返回数值）
local pw = tonumber(Properties["pulse_width"].Value) or 0.3
```
**注意**：设计时函数（GetControls/GetControlLayout）中用 `props["name"].Value`，运行时用 `Properties["name"].Value`

### 20. PluginInfo.Id 冲突（致命）
**症状**：插件分类消失，找不到模块，无明显语法错误
**根因**：两个 qplug 文件使用了相同的 `PluginInfo.Id`。Q-SYS 用 Id 唯一标识插件，Id 冲突导致加载失败
**解决**：每个插件必须使用唯一 GUID。用 `[guid]::NewGuid().ToString()` (PowerShell) 或 `uuidgen` 生成
**检查**：定期检查 Plugins 目录下所有文件的 Id 是否重复
```powershell
Get-ChildItem *.qplug | ForEach-Object { if ((Get-Content $_.FullName -Raw) -match 'Id\s*=\s*"([^"]+)"') { "$($_.Name): $($Matches[1])" } }
```

## 调试技巧

- 用 `print()` 输出到 Q-SYS 控制台
- 面板上放 monitor_log Text 控件显示结构化日志
- 日志格式：`HH:MM:SS [流向] [类型 方向 编号] = 值`
- 修改 qplug 后必须删除旧组件重新拖入（属性变更不会热更新）
- Python 验证脚本：检查括号匹配、控件名引用一致性
