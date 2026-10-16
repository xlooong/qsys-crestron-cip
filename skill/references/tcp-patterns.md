# TCP 通信模式

## 标准 TCP 客户端模式

```lua
local tcp = nil
local isConnected = false
local userDisconnected = false  -- 区分用户主动断开 vs 意外断开
local reconnectTimer = Timer.New()
local RECONNECT_INTERVAL = 5

-- 连接
function doConnect()
  if tcp then tcp:Disconnect(); tcp = nil end
  tcp = TcpSocket.New()
  tcp.EventHandler = function(s, eventType)
    if eventType == "CONNECTED" then
      isConnected = true
      -- 启动数据轮询和心跳
    elseif eventType == "CLOSED" then
      isConnected = false
      if not userDisconnected then
        reconnectTimer:Start(RECONNECT_INTERVAL)
      end
    elseif eventType == "ERROR" then
      isConnected = false
      if not userDisconnected then
        reconnectTimer:Start(RECONNECT_INTERVAL)
      end
    end
  end
  tcp:Connect(ip, port)
end

-- 断开（用户主动）
function doDisconnect()
  userDisconnected = true
  if tcp then tcp:Disconnect(); tcp = nil end
  isConnected = false
end

-- 重连定时器
reconnectTimer.EventHandler = function()
  reconnectTimer:Stop()
  if not userDisconnected then
    doConnect()
  end
end

-- 启动时自动连接
doConnect()
```

## 粘包处理

```lua
local rxBuffer = ""
local pollTimer = Timer.New()

pollTimer.EventHandler = function()
  if not isConnected or not tcp then return end
  local data = tcp:Read(4096)
  if data then rxBuffer = rxBuffer .. data end

  -- 按协议长度字段拆包
  while #rxBuffer >= 4 do
    local lenH = rxBuffer:byte(2)
    local lenL = rxBuffer:byte(3)
    local totalLen = 3 + (lenH * 256 + lenL)
    if #rxBuffer < totalLen then break end
    parsePacket(rxBuffer:sub(1, totalLen))
    rxBuffer = rxBuffer:sub(totalLen + 1)
  end
end
pollTimer:Start(0.05)
```

## 心跳超时 Watchdog（两级）

```lua
local lastDataTime = 0
local lastSignalTime = 0
local regCompleteTime = 0
local watchdogTimer = Timer.New()
local WATCHDOG_TIMEOUT = 20   -- 无任何数据
local POST_REG_TIMEOUT = 15   -- 注册后无信号数据

-- 收到任何数据时更新
lastDataTime = os.time()

-- 收到数字/模拟/串量时更新
lastSignalTime = os.time()

-- 注册成功时记录
regCompleteTime = os.time()

watchdogTimer.EventHandler = function()
  if not isConnected or userDisconnected then return end
  local now = os.time()
  -- Level 1: TCP 假连接
  if now - lastDataTime > WATCHDOG_TIMEOUT then
    forceReconnect("no data for " .. (now - lastDataTime) .. "s")
    return
  end
  -- Level 2: CIP 假会话（注册成功但无信号）
  if isRegistered and regCompleteTime > 0 then
    local ref = lastSignalTime > regCompleteTime and lastSignalTime or regCompleteTime
    if now - ref > POST_REG_TIMEOUT then
      forceReconnect("fake CIP session, no signal for " .. (now - ref) .. "s")
    end
  end
end
watchdogTimer:Start(5)
```

## CIP 协议要点

### 注册流程
1. TCP 连接到 41794 端口
2. 等待 0x0F Program Ready（可选，3 秒超时后直接注册）
3. 发送 IPID 注册包：`01 00 0B 00 00 00 00 00 <IPID> 40 FF FF F1 01`
4. 收到 0x02 注册响应
5. 发送更新请求：`05 00 05 00 00 02 03 00`
6. 启动 15 秒心跳

### 包类型
| 类型 | 含义 | 处理 |
|------|------|------|
| 0x02 | 注册响应 | 设置 isRegistered |
| 0x03 | 对端断开 | 强制重连（非用户断开） |
| 0x05 | 数据帧 | 解析子包（数字/模拟） |
| 0x0D | 心跳请求 | 回复 0x0E |
| 0x0E | 心跳响应 | 忽略 |
| 0x0F | 程序状态 | 就绪后注册 |
| 0x12 | 扩展帧 | 解析串量 |

### 数字量包
```
05 00 06 00 00 03 00 <join_low> <join_high+flag>
flag: 0x00=true, 0x80=false
join = (join_high & 0x7F) * 256 + join_low + 1
```

### 模拟量包
```
05 00 08 00 00 05 14 <join_high> <join_low> <value_high> <value_low>
value = value_high * 256 + value_low (0-65535)
```

### 串量包
```
12 <len_high> <len_low> 00 00 00 <payload_len> 34 <join_high> <join_low> 03 <string...>
```

## Trigger 脉冲拉伸

```lua
local digitalPulseTimers = {}
local PULSE_WIDTH = 0.3  -- 属性可配置

function sendDigital(join, value)
  -- 发送 CIP 包
  -- 如果是 true，启动定时器自动设回 false
  if value then
    if digitalPulseTimers[join] then digitalPulseTimers[join]:Stop() end
    digitalPulseTimers[join] = Timer.New()
    digitalPulseTimers[join].EventHandler = function()
      digitalPulseTimers[join]:Stop()
      sendDigitalRaw(join, false)
    end
    digitalPulseTimers[join]:Start(PULSE_WIDTH)
  end
end
```
