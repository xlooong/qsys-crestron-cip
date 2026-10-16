# Lua Scripting in Q-Sys

> 来源: 《Lua Scripting in Q-Sys: A Guide for Navigating the Wide World of Control Scripting》
> 作者: Aaron Hood, The Farm AV (1st Edition)
> 页数: 31页
> 用途: Q-SYS Lua 脚本开发完整入门指南

---

## 1. Getting Started

### 1.1 The Print Function

```lua
print("Hello, world!")           -- 单条语句，自动换行
print("Hello", "world!")         -- 多条语句，空格分隔
```

### 1.2 Types of Data in Q-Sys

#### Comments and nil

```lua
-- This is a single-line comment
--[[ This is a
multi-line comment ]]
```

`nil` 是 Lua 中的特殊值，表示不存在。引用不存在的变量返回 nil。

#### Booleans

```lua
print(true)       --> true
print(false)      --> false
print(not false)  --> true

-- 比较运算符返回 boolean
print(1==1, 1 ~= 1, 1 > 0, 1 >= 0, 1 < 0, 1 < 0)
--> true  false  true  true  false  false

-- 字符串相等比较
print("cat" == "dog")  --> false
```

#### Numbers

整数和小数两种。Lua 总是优先用小数形式打印。算术运算：`+ - * / ^ %`（加、减、乘、除、幂、取模）。

#### Strings

字符串是字符数组，可包含可读字符和十六进制码。转义序列：

| 转义 | 用途 |
|------|------|
| `\a` | Bell |
| `\b` | Backspace |
| `\f` | Formfeed |
| `\n` | New Line |
| `\r` | Carriage Return |
| `\t` | Tab |
| `\v` | Vertical Tab |
| `\\` | Backslash |
| `\"` | Double Quote |
| `\'` | Single Quote |

### 1.3 Tables And Arrays

#### Arrays

整数索引，从 1 开始：

```lua
testArray = {"cat", 34}
print(testArray[1], testArray[2])  --> cat  34

table.concat(testArray, " ")       --> "cat 34"
table.insert(testArray, "tree")    -- 插入末尾
table.remove(testArray, 2)         -- 移除第2个，返回被移除项
print(#testArray)                  --> 2 (长度)
```

#### Tables

键值对：

```lua
-- 简单方式（键不能有空格）
testTable = {cat = "meow", dog = "woof"}

-- 生成方式（键不能有空格）
testTable = {}
testTable.cat = "meow"

-- 推荐方式（键可以有空格）
testTable = {}
testTable["cat"] = "meow"
testTable["blue jay"] = "squawk"
```

#### Multidimensional Tables

```lua
testTable = {
  ["fruits"] = {"apple", "orange", "banana"},
  ["vegetables"] = {"carrot", "lettuce", "fennel"}
}
print(testTable.fruits[1], testTable["vegetables"][3])
--> apple  fennel
```

### 1.4 Logic

```lua
if cat == dog then
  print("The dog is a cat")
elseif dave == cat then
  print("Dave is pretending to be a cat")
else
  print("Neither")
end
```

**重要**: 逻辑分支按顺序匹配，第一个满足的分支执行后跳过其余。应将最具体的条件放在前面，`else` 作为通用情况或兜底。

### 1.5 Looping

```lua
num = 0
for i = 1, 5 do
  num = num + i
end
print(num)  --> 15

-- 遍历数组
for i = 1, #testArray do
  print(testArray[i])
end

-- 遍历表（pairs 不保证顺序）
for key, value in pairs(testTable) do
  print(key, value)
end
```

### 1.6 String Manipulation

#### Concatenation

```lua
first = "this"
second = "that"
print(first..second)  --> thisthat
```

#### Numerical Codes

```lua
print(string.byte("t"))   --> 116
print(string.char(116))   --> t
```

用于校验和计算。

#### String Length

```lua
str = "this"
print(string.len(str))  --> 4
```

#### Case Changers

```lua
print(string.upper("this"))  --> THIS
print(string.lower("THIS"))  --> this
```

#### Patterns（模式匹配）

字符类：

| 模式 | 含义 |
|------|------|
| `.` | 所有字符 |
| `%a` | 所有字母 |
| `%c` | 所有控制字符 |
| `%d` | 所有数字 |
| `%l` | 所有小写字母 |
| `%p` | 所有标点 |
| `%s` | 所有空格 |
| `%u` | 所有大写字母 |
| `%w` | 所有字母数字 |
| `%x` | 所有十六进制数字 |
| `%z` | Zero |
| `[set]` | 集合中的字符 |
| `[^set]` | 不在集合中的字符 |

序列修饰符：

| 修饰符 | 含义 |
|--------|------|
| `+` | 一次或多次（最长匹配） |
| `*` | 零次或多次（最长匹配） |
| `-` | 零次或多次（最短匹配） |
| `?` | 零次或一次 |

#### string.format

```lua
print(string.format("The string is: \"%s\". The float is: %f. The integer is: %d.",
  "Hello!", 2.71828, 21))
--> The string is: "Hello!". The float is: 2.718280. The integer is: 21.
```

#### string.find

```lua
str = "this is a string"
print(string.find(str, "%a+"))        --> 1  4 (第一个词 this)
print(string.find(str, "not in str")) --> nil
print(string.find(str, "%a+", 5))     --> 6  7 (从位置5开始找)
```

#### string.sub

```lua
str = "this is a string"
print(string.sub(str, 1, -8))  --> this is a  (从开头到倒数第8个字符)
```

#### string.match / string.gmatch

```lua
print(string.match(str, "%a+"))       --> this (返回匹配的子串)
print(string.match(str, "%a+", 5))    --> is

for s in string.gmatch(str, "%a+") do  -- 遍历所有匹配
  print(s)
end
--> this / is / a / string
```

#### tonumber

```lua
str = "12"
num = tonumber(str)
print(num, num + 1)  --> 12  13
```

#### 另一种语法

```lua
str = "this is a string"
print(str:match("%a+"))  --> this  (冒号语法，隐式传入 str)
```

### 1.7 Functions

```lua
function add(arg1, arg2)
  return arg1 + arg2
end
print(add(1, 4))  --> 5
```

**注意**: 不能在函数声明之前调用它（类似变量）。

#### os.date and os.time

`os.time` 返回表：

| Key | Values |
|-----|--------|
| year | Full year |
| month | 01-12 |
| day | 01-31 |
| hour | 00-23 |
| min | 00-59 |
| sec | 00-59 |
| isdst | Boolean: true if daylight savings |

`os.date` 格式化标签：

| Tag | Return |
|-----|--------|
| `%a` | 缩写星期 (Mon) |
| `%A` | 完整星期 |
| `%b` | 缩写月份 (Jan) |
| `%B` | 完整月份 |
| `%c` | 日期时间 (08/15/2021 17:43:08) |
| `%d` | 日 |
| `%H` | 24小时制 |
| `%I` | 12小时制 |
| `%M` | 分钟 |
| `%m` | 月份 |
| `%p` | am/pm |
| `%S` | 秒 |
| `%w` | 星期 0-6 (Sunday-Saturday) |
| `%x` | 日期 (08/15/2021) |
| `%X` | 时间 (01:31:55) |
| `%Y` | 完整年份 |
| `%y` | 两位年份 |

---

## 2. Coding for Q-Sys

### 2.1 Controls IO

```lua
-- Control Script 方式
led = Controls.Inputs[1]
status = Controls.Outputs[1]

-- Text Controller 自定义名称
led = Controls.LED
status = Controls["Status Output"]
```

**重要**: 将控件赋值给变量时，变量保存的是控件的引用（函数表），不是当前值。访问值时应在需要时才读取，否则可能使用过期值。

#### EventHandler

```lua
Controls.Inputs[1].EventHandler = function()
  print("My value was changed!")
end
```

#### Boolean

```lua
Controls.Inputs[1].EventHandler = function()
  print(Controls.Inputs[1].Boolean)
end

-- if 语句中可直接用 boolean 控件
if Controls.Inputs[1].Boolean then
  print("the button is on")
end
```

**注意**: 非 trigger 按钮有独立的 on/off 状态，EventHandler 中必须包含逻辑分支区分两种状态。

#### Value

```lua
Controls.fader.EventHandler = function()
  print(Controls.fader.Value)
end
```

#### String

```lua
Controls.str_input.EventHandler = function()
  print(Controls.str_input.String)
end
```

**注意**: 当字符串控件被改为与之前相同的字符串时，EventHandler 不会被调用。

#### Status

Status 控件是 integer + string 的组合。integer 码对应状态：

| Number | Status |
|--------|--------|
| 0 | OK |
| 1 | Compromised |
| 2 | Fault |
| 3 | Not Present |
| 4 | Missing |
| 5 | Initializing |

```lua
Controls.stat.Value = 3
Controls.stat.String = "I can't Find it!"
```

#### Values（数组）

RTA 输出等控件的值以数组形式访问：`Controls.RTA.Values[5]`

#### Color

```lua
Controls.Button.Color = "blue"       -- 文字颜色名
Controls.Button.Color = "#0000FF"    -- 十六进制
```

#### Control Count

多计数控件的相关控件函数放在数组中：`Controls.text_inputs[3].String`

### 2.2 Timers

#### Timer Entity

```lua
count = 0
counter = Timer.New()
counter.EventHandler = function()
  if count < 3 then
    count = count + 1
    print(count)
  else
    counter:Stop()
    count = 0
    print("Finished Counting.")
  end
end
counter:Start(1)  -- 每1秒触发
```

#### Timer.CallAfter

```lua
Timer.CallAfter(function()
  print("This was delayed by 1.5 seconds")
end, 1.5)
```

#### Temporal Sequences

```lua
-- Timer Entity 方式
seq = 0
s_timer = Timer.New()
s_timer.EventHandler = function()
  if seq == 0 then first_func()
  elseif seq == 1 then second_func()
  elseif seq == 2 then third_func()
  else s_timer:Stop(); seq = 0; return
  end
  seq = seq + 1
end
s_timer:Start(1)

-- 嵌套 Timer.CallAfter 方式
Timer.CallAfter(function()
  first_func()
  Timer.CallAfter(function()
    second_func()
    Timer.CallAfter(function()
      third_func()
    end, 1)
  end, 1)
end, 1)
```

### 2.3 Components

#### Initializing

```lua
mixer = Component.New("Near-End Mixer")
```

#### Viewing Accessible Controls

Tools → View Component Control Info，查看组件可访问的控件名。

#### Accessing Controls

```lua
mixer = Component.New("Near-End Mixer")
print(mixer["input.1.gain"].Value)  --> 0.0
```

#### Organizing Controls（构建控件表）

```lua
mixerComp = Component.New("Near-End Mixer")
mixer = { inputs = {}, outputs = {} }

for i = 1, 8 do
  mixer.inputs[i] = {
    gain   = mixerComp["input." .. i .. ".gain"],
    invert = mixerComp["input." .. i .. ".invert"],
    label  = mixerComp["input." .. i .. ".label"],
    mute   = mixerComp["input." .. i .. ".mute"],
    solo   = mixerComp["input." .. i .. ".solo"],
    trim   = mixerComp["input." .. i .. ".trim"],
  }
  mixer.outputs[i] = {
    gain   = mixerComp["output." .. i .. ".gain"],
    invert = mixerComp["output." .. i .. ".invert"],
    label  = mixerComp["output." .. i .. ".label"],
    mute   = mixerComp["output." .. i .. ".mute"],
    prepost = mixerComp["output." .. i .. ".pre.post"],
  }
end

-- 使用
for i = 1, #mixer.inputs do
  mixer.inputs[i].gain.EventHandler = function()
    if mixer.inputs[i].gain.Value < -40 then
      mixer.inputs[i].mute.Boolean = true
    end
  end
end
```

### 2.4 User Interface

#### UCI Functions（在 Designer 中可见）

**Uci.SetLayerVisibility**

```lua
Uci.SetLayerVisibility(
  "User UCI",      -- UCI 名
  "Audio Page",    -- 页面名
  "Fader Layer",   -- 层名
  vis_button.Boolean,  -- 是否可见
  "none"           -- 过渡: none/fade/left/right/bottom/top
)
```

**Uci.SetSharedLayerVisibility** — 影响所有页面的共享层，不需要页面名参数。

#### Touch Panel And UCI Viewer Functions

**Uci.ShowDialog** — 弹出对话框：

```lua
function switchInput(choiceInt)
  print("Input "..choiceInt.." was picked")
  send_input_cmd(choiceInt)
end

function ShowInputDialog()
  Uci.ShowDialog("User UCI", {
    Title = "Input Selection",
    Message = "Select your desired input",
    Buttons = {"HDMI 1", "HDMI 2", "DisplayPort"},
    Handler = switchInput
  })
end
```

**Uci.SetScreen** — 设置屏幕状态（On/Off/Dim）：
```lua
Uci.SetScreen("User Touch Panel", "Dim")
```

**Uci.SetUCI** — 需要 Dynamic UCI Assignment 属性启用：
```lua
Uci.SetUCI("User Touch Panel", "User Login UCI")
```

**Uci.SetPage** — 切换页面：
```lua
Uci.SetPage("User Touch Panel", "Home Page")
```

**Uci.LogOff** — 注销触摸屏：
```lua
Uci.LogOff("User Touch Panel")
```

### 2.5 Serial Ports

串口连接第三方设备。**重要**: 必须查看设备的串口控制 API 手册确认波特率、数据位、校验位。默认 9600 8N1。

### 2.6 TcpSocket and TcpSocketServer

TCP Socket 是控制第三方设备的首选方式。TcpSocketServer 用于在特定端口监听其他设备的控制消息。

### 2.7 JSON

```lua
json = require("json")
luaTable = { array = {"a", "b", "c"}, table = {a=1, b=2, c=3} }
jsonTable = json.encode(luaTable)
print(jsonTable)
--> {"table":{"c":3,"b":2,"a":1},"array":["a","b","c"]}
```

### 2.8 HttpClient

**Upload (POST/PUT)**:

```lua
URL = "https://www.example.com/"
function handleResponse(tbl, code, data, err)
  print("Response Code: "..code)
  print("Errors: "..err or "None")
  print("Data: "..data)
end

HttpClient.Upload {
  Url = URL,
  Method = "POST",
  User = "username",
  Password = "password",
  Data = "message body",
  EventHandler = handleResponse
}
```

**Download (GET)**:

```lua
function handleDownload(tbl, code, data, err, headers)
  print("Response Code: "..code)
  for headerName, headerContent in pairs(headers) do
    print(headerName.." = "..headerContent)
  end
  print("Data: "..data)
end

HttpClient.Download {
  Url = URL,
  Headers = {["Content-Type"] = "text/html"},
  Timeout = 30,
  EventHandler = handleDownload
}
```

---

## 3. Building a Text Controller

### 3.1 The Plan of Attack（开发前6个问题）

1. **期望功能是什么?** — 列出完整详细的功能清单，作为 checklist
2. **需要额外组件吗?** — 考虑涉及的物理设备和处理组件
3. **可以添加增强功能吗?** — 额外功能带来更多 bug 风险，区分"哇"功能和简单按钮
4. **最大的开发挑战是什么?** — 分解功能为基础组件，按难度排序，从最难开始
5. **有现有程序可作起点吗?** — 复用代码时注意上下文适配
6. **程序应该静态还是动态结构?** — 根据是否需要可扩展性决定

### 3.2 Control Structures（控件表组织）

将相关控件存储在多维表中：

```lua
cTable = { Button = {}, Led = {}, Text = {} }

for i = 1, #Controls.Button do
  cTable.Button[i] = Controls.Button[i]
  cTable.Led[i] = Controls.LED[i]
  cTable.Text[i] = { ctl = Controls.Text[i] }
  cTable.Text[i].clear = function()
    Timer.CallAfter(function()
      cTable.Text[i].ctl.String = ""
    end, 2)
  end

  cTable.Button[i].EventHandler = function()
    cTable.Led[i].Boolean = cTable.Button[i].Boolean
    if cTable.Button[i].Boolean then
      cTable.Text[i].ctl.String = "ON"
    else
      cTable.Text[i].ctl.String = "POWERING OFF"
      cTable.Text[i].clear()
    end
  end
end
```

---

## 4. Advanced Concepts

### 4.1 Checksum Algorithms & Command Composition

```lua
eoc = "\r"  -- 全局 EOC 变量

-- 校验和算法
function checksum(cmd)
  local sum = 0
  for c in cmd:gmatch("%x") do
    sum = sum + string.byte(c)
  end
  return sum
end

-- 命令组装
function compose(cmd)
  local cLength = cmd:len()
  local cSum = checksum(cmd)
  return cLength .. cmd .. cSum .. eoc
end
```

### 4.2 3rd-Party Feedback（控件表结构）

```lua
cTable = {
  pwr = {
    ctl = Controls.Power,
    Type = "Boolean",
    cmd = "\x01",
    par = { off = "\x00", on = "\x01" },
    handle = function(par)
      if par == "\x00" then cTable.ctl[Type] = true
      else cTable.ctl[Type] = false end
    end
  },
  vol = {
    ctl = Controls.Volume,
    Type = "Value",
    cmd = "\x02",
    par = vol.ctl[Type],
    handle = function(par)
      vol.ctl[Type] = string.byte(par)
    end
  }
}

address = Controls["IP Address"]
port = Controls.Port
status = Controls.Status
socket = TcpSocket.New()

socket.Data = function(socket)
  local data = socket:Read(socket.BufferLength)
  local inCmd = data:sub(2,2)   -- 命令名在第2个字符
  local inPar = data:sub(3)     -- 参数在第3个字符
  for k, tbl in pairs(cTable) do
    if inCmd == tbl.cmd then
      tbl.handle(inPar)
      return
    end
  end
  print("Warning: "..data.." is not in the command table (cTable)")
end

function connect()
  socket:Connect(address.String, port.Value)
end
address.EventHandler = connect
port.EventHandler = connect
connect()
```

### 4.3 Confirm Button（可变参数函数）

```lua
confirm = function(...)
  Controls.Confirm.Color = "yellow"
  local arg = {...}
  local func = table.remove(arg, 1)
  for i = 1, #arg do
    if arg[i] == nil then table.remove(arg, i) end
  end
  Controls.Confirm.EventHandler = function()
    Controls.Confirm.Color = "white"
    func(table.unpack(arg))
    Controls.Confirm.EventHandler = nil
  end
end

cancel = function()
  Controls.Confirm.Color = "white"
  Controls.Confirm.EventHandler = nil
end

-- 应用示例
function otherprint(string1, string2, string3)
  print(string1..string2..string3)
end
confirm(otherprint, "hi ", "there, ", "friend!")
```

---

## 关键要点总结

1. **控件值访问**: 不要将控件值缓存到变量，应在需要时通过 `.Boolean`/`.Value`/`.String` 实时读取
2. **EventHandler**: 非 trigger 按钮必须区分 on/off 两种状态
3. **字符串相同不触发**: String 控件被设为相同值时 EventHandler 不调用
4. **Timer**: `Timer.New()` + `:Start(seconds)` 用于重复；`Timer.CallAfter(func, seconds)` 用于单次延迟
5. **Component**: 用 `Component.New("Label")` 访问设计中的组件控件
6. **控件表组织**: 用多维表组织相关控件，便于批量操作和遍历
7. **第三方反馈**: 构建命令表（cmd + handle函数），收到数据后查表分发
8. **os.date/os.time**: 用于定时调度和时间判断
