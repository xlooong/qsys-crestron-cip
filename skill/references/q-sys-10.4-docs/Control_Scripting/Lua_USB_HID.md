# Lua USB HID

> 来源: https://help.qsys.com/q-sys_10.4/#Control_Scripting/Lua_USB_HID.htm
> 入库时间: 2026-10-16
> 用途: Q-SYS Lua USB HID 设备输入

> **注意**: 由于 USB 设备种类繁多，使用此功能需自担风险。QSC 无法保证与所有 USB HID 外设兼容。

## 概述 / Overview

Q-SYS 提供两个内置 Lua 库，用于接收连接到 Q-SYS Core 处理器 USB-A 端口的 USB HID（人机接口设备）外设的输入事件：

| 库 | 功能 |
|----|------|
| **UsbMonitor** | 检测 USB HID 设备插入/移除 |
| **Uab** | 接收单个 USB 设备的输入事件（按键、轴移动、按钮点击等） |

## UsbMonitor

监控 Core 上 USB HID 设备的连接和断开。

### .New("Input")

实例化新实例。

```lua
monitor = UsbMonitor.New("Input")
```

### .EventHandler

设备添加/移除到 Core 时调用。

```lua
monitor.EventHandler = function(devInfo)
```

### 示例负载 / Example Payloads

```json
{
  "devnode": "/dev/input/event2",
  "name": "Q-00000000",
  "product": "QSC USB HID Keyboard",
  "vendor": "QSC Inc",
  "bus": "usb",
  "modalias": "usb:v05FCp000Cd0100dc00dsc00dp00ic03isc01ip00in00",
  "uniq": "",
  "actions": {
    "add": "/devices/pci0000:00/0000:00:14.0/usb3/3-1/3-1.1/3-1.1:1.0/input/input2/event2"
  }
}
```

## Uab（Usb 库）

处理单个 USB 设备，类似 TcpSocketServer 中的 TCP Socket。

### .New(devnode)

```lua
local device = Uab.New(devnode)
```

| 参数 | 类型 | 说明 |
|------|------|------|
| devnode | string | 设备节点路径。HID 设备必须以 `/dev/input/event` 开头；串口 USB 设备以 `/dev/tty` 开头 |

## 枚举 / Enumerators

USB 事件类型查找表（来源: kernel.org event-codes.txt）：

| 名称 | 值 | 说明 |
|------|-----|------|
| EV_SYN | 0 | 同步事件 |
| EV_KEY | 1 | 按键事件 |
| EV_REL | 2 | 相对轴事件 |
| EV_ABS | 3 | 绝对轴事件 |
| EV_MSC | 4 | 杂项事件 |
| EV_SW | 5 | 开关事件 |
| EV_LED | 17 | LED 事件 |
| EV_SND | 18 | 声音事件 |
| EV_REP | 20 | 重复事件 |
| EV_FF | 21 | 力反馈事件 |
| EV_PWR | 22 | 电源按钮和开关输入专用 |
| EV_FF_STATUS | 23 | 力反馈状态 |

### 查询示例

```lua
-- 按键码查找
local code = usb.key.KEY_BACKSPACE

-- 按键名反查
function getKeyName(code)
  for k, v in pairs(usb.key) do
    if v == code then
      return k
    end
  end
  return nil
end
```

### 查找表

- **Sync**: SYN_REPORT=0, SYN_CONFIG=1, SYN_MT=2, SYN_DROPPED=3
- **Relative**: REL_X=0, REL_Y=1, REL_Z=2, REL_RX=3, REL_RY=4, REL_RZ=5, REL_HWHEEL=6, REL_DIAL=7, REL_WHEEL=8, REL_MISC=9
- **Absolute**: ABS_X=0, ABS_Y=1, ABS_Z=2, ABS_RX=3, ABS_RY=4, ABS_RZ=5, ABS_THROTTLE=6, ABS_RUDDER=7, ABS_WHEEL=8, ABS_GAS=9, ABS_BRAKE=10, ABS_HAT0X=16, ABS_HAT0Y=17, ABS_HAT1X=18, ABS_HAT1Y=19, ABS_HAT2X=20, ABS_HAT2Y=21, ABS_HAT3X=22, ABS_HAT3Y=23, ABS_PRESSURE=24, ABS_DISTANCE=25, ABS_TILT_X=26, ABS_TILT_Y=27, ABS_TOOL_WIDTH=28, ABS_VOLUME=32, ABS_MISC=40, ABS_MT_SLOT=47, ABS_MT_TOUCH_MAJOR=48, ABS_MT_TOUCH_MINOR=49, ABS_MT_WIDTH_MAJOR=50, ABS_MT_WIDTH_MINOR=51, ABS_MT_ORIENTATION=52, ABS_MT_POSITION_X=53, ABS_MT_POSITION_Y=54, ABS_MT_TOOL_TYPE=55, ABS_MT_BLOB_ID=56, ABS_MT_TRACKING_ID=57, ABS_MT_PRESSURE=58, ABS_MT_DISTANCE=59, ABS_MT_TOOL_X=60, ABS_MT_TOOL_Y=61
- **Switch**: SW_LID=0, SW_TABLET_MODE=1, SW_HEADPHONE_INSERT=2, SW_RFKILL_ALL=3, SW_MICROPHONE_INSERT=4, SW_DOCK=5, SW_LINEOUT_INSERT=6, SW_JACK_PHYSICAL_INSERT=7, SW_VIDEOOUT_INSERT=8, SW_CAMERA_LENS_COVER=9, SW_KEYPAD_SLIDE=10, SW_FRONT_PROXIMITY=11, SW_ROTATE_LOCK=12, SW_LINEIN_INSERT=13
- **Misc**: SERIAL=0, PULSE=1, CLOCK=2, GPS=3, UNDEF=4, TIMESTAMP=5
- **Led**: LED_NUML=0, LED_CAPSL=1, LED_SCROLLL=2, LED_COMPOSE=3, LED_KANA=4, LED_SLEEP=5, LED_SUSPEND=6, LED_MUTE=7, LED_MISC=8, LED_MAIL=9, LED_CHARGING=10
- **Repeat**: DELAY=0, PERIOD=1
- **Sound**: CLICK=0, BELL=1, TONE=2
- **FF**: STATUS_STOPPED=0, STATUS_PLAYING=1
- **Key**: 完整标准 Linux 键码表（KEY_0=48 ... KEY_F24=135, KEY_LSHIFT=160 等），查找方式 `usb.key.KEY_BACKSPACE`

## EventHandler

函数调用时带一个含 3 个条目的表：

```lua
1 type = (integer),   -- 事件类型（EV_* 枚举）
2 code = (integer),   -- 事件码
3 value = (integer)   -- 事件值
```

## 推荐实践 / Recommended Practices

1. **USB 设备应全局作用域或赋值给全局表**，避免垃圾回收问题
2. **usb.EventHandler 可能无数据调用**，需检查参数是否为 nil

```lua
function usb_data_handler( data )
  if data then
    -- 处理数据
  end
end
```

## Helper Lua Module 示例

```lua
local usbhelpers = {}

usbhelpers.gettype = function(code)
  for k,v in pairs(usb.types) do
    if v == code then return k end
  end
  return nil
end

usbhelpers.getdesc = function(code)
  for k,v in pairs(usb.desc) do
    if v == code then return k end
  end
  return nil
end

usbhelpers.getrelative = function(code)
  for k,v in pairs(usb.relative) do
    if v == code then return k end
  end
  return nil
end

usbhelpers.getabsolute = function(code)
  for k,v in pairs(usb.absolute) do
    if v == code then return k end
  end
  return nil
end

usbhelpers.actions = {
  [1] = "Released",
  [2] = "Pressed",
  [3] = "Hold"
}

return usbhelpers
```

## 完整示例

```lua
monitor = require("monitor")
usbhelpers = require("usbhelpers")
usbmonitor = UsbMonitor.New("input")

function usb_data_handler(data)
  print(inspect(data))
  print(usbmonitor:getDeviceType())
  print(usbhelpers.getActive(data))
  local btn = usbhelpers.getButton(data)
  if btn then
    print("Button: "..btn)
    print(usbhelpers.getToggle(data))
    print(usbhelpers.getLed(data))
    print(usbhelpers.getSound(data))
    print(usbhelpers.getForceFeedback(data))
    print(usbhelpers.getKey(data))
  end
end

usbmonitor:addEventHandler(usb_data_handler)

function usbmonitor:onInit()
  print("USB Monitor initialized")
  local device = usbmonitor:getDevice()
  local model = device:getProperties().Model
  if model == "USB Device" then
    usbmonitor:setEventHandler(usb_data_handler)
  else
    device:removeEventHandler(usb_data_handler)
    usbmonitor:setEventHandler(function() end)
  end
end
```

## 要点 / Key Points

- 两个库：UsbMonitor（设备插拔检测）+ Uab（单设备输入事件）
- devnode 以 `/dev/input/event` 开头（HID）或 `/dev/tty` 开头（串口 USB）
- 事件回调表：type/code/value 三个整数
- 设备对象必须全局作用域防垃圾回收
