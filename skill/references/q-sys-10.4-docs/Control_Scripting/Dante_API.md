# Dante API

> 来源: https://help.qsys.com/q-sys_10.4/#Control_Scripting/Dante_API.htm
> 入库时间: 2026-10-16
> 用途: Q-SYS Lua Dante GPIO 控制

## 概述 / Overview

Dante API (DAPI) 由两个模块组成，用于从 Q-SYS Lua 脚本与 Dante 设备的 GPIO 接口通信。

> **注意**: 初始 Dante 设备支持仅限 Audio-Technica 麦克风。其他使用 DAPI 进行 GPIO 控制的 Dante 设备可能可用但未经测试。这是一个通用接口，设备上 GPIO 的实际用法取决于被控设备。

## Dante Domain Manager 与设备发现

### Core 未加入 DDM（Dante Domain Manager）

- **设备发现**: Core 会发现同一网络上所有未加入任何 DDM 域的 Dante 设备。不会发现已加入 DDM 域的设备（这些设备由 DDM 管理和隔离）。

### Core 已加入 DDM

- **设备发现**基于 Core 加入的域：
  - **同域**: 发现所有加入同一 DDM 域的设备
  - **跨域**: 不会自动发现其他 DDM 域的设备，除非配置允许跨域通信
  - **未启用**: 不会发现未加入任何 DDM 域的设备（在 DDM 管理范围之外）

DDM 本质上创建了受控环境，只有同域设备可互相通信，增强安全性和管理能力。

## DanteBrowser

创建浏览器对象，发现网络上的 Dante 设备。用于确认设备是否存在于网络上。

### 语法

```lua
browser = DanteBrowser.New()
```

### 属性/函数

| 成员 | 说明 |
|------|------|
| `.Browser` | 返回的对象可被赋值回调函数。设备添加/移除时调用。参数：设备名 + 事件类型（"ADDED", "REMOVED"） |

> **注意**: DanteBrowser 依赖底层 Audinate 库提供信息。REMOVED 回调在设备移除后可能需要不确定的时间才会触发。

## DanteDevice

创建对象，访问网络上特定设备。允许脚本设置设备 GPIO 状态（如点亮 LED）以及接收 GPIO 事件（如设备上按钮按下）。

### 语法

```lua
device = DanteDevice.New(deviceName)
```

### 属性/函数

| 成员 | 说明 |
|------|------|
| `:Device(value, mask)` | 设置设备 GPIO 状态。value 和 mask 为整数。返回数值型调用 ID |
| `:GetGpio()` | 请求 GPIO 当前状态。返回数值型调用 ID |
| `.Gpio` | GPIO 状态变化时的回调函数。接收一个包含 GPIO 状态详情的表：<br>- `.TriggerMask` - 变化的位掩码<br>- `.InputMask` - 设为输入的引脚位掩码<br>- `.InputValue` - 输入引脚的值<br>- `.OutputMask` - 设为输出的引脚位掩码<br>- `.OutputValue` - 输出引脚的值 |
| `.Response` | 判断调用是否成功的回调。两个参数：ID 和 errorString。后者在成功时为 nil |

> **注意**: 即使没有返回 errorString，也不能保证调用到达设备；但 errorString 存在则一定发生了错误。

| 成员 | 说明 |
|------|------|
| `.EventHandler` | 订阅 KeepAlive 通道的回调函数，允许在设备连接丢失/建立时接收事件。参数：设备名 + 事件类型（"CONNECTION", "NO_CONNECTION"） |

## 示例：Audio-Technica 麦克风 GPIO

### GPIO 分配表

| 功能 | GPIO # | GPIO 值 (0) | GPIO 值 (1) | 方向 |
|------|--------|-------------|-------------|------|
| LOCAL/REMOTE | GPIO 0 | LOCAL | REMOTE | IN |
| ACTIVATION/TWIST | GPIO 1 | ON | CLOSED | OUT |
| GREEN LED | GPIO 2 | OFF | ON | IN |
| RED LED | GPIO 3 | OFF | ON | IN |
| GAIN | GPIO 4 | 0dB | Mute | IN |
| GAIN | GPIO 5 | 10-40 | 10-40 | IN |
| LOW CUT | GPIO 6 | OFF | ON | IN |
| PHANTOM POWER** | GPIO 7 | OFF | ON | IN |

> **注意**: Phantom Power 控制仅部分型号可用

- GPIO 0, 2, 3, 4, 5, 6, 7 配置为**输入**（可被外部拉高/拉低）
- GPIO 1 配置为**输出**（可被读取/通知）

### 控制说明

GPIO 0 用于切换 LOCAL/REMOTE 模式。LOCAL 模式下，静音按钮本地控制麦克风音频和 LED。要从脚本控制麦克风，需先将 GPIO 0 设为 1 切换为 REMOTE 模式（发送 value=01, mask=01）。

示例脚本同步本地静音状态按钮与麦克风上的远程按钮和 LED。

## 要点 / Key Points

- DAPI 用于控制 Dante 设备 GPIO（LED、按钮、静音等）
- 支持 DDM 域的设备发现隔离
- 用 mask 定位要修改的 GPIO 位
- 初始仅支持 Audio-Technica 麦克风
