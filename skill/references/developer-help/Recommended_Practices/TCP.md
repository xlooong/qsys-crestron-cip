# TCP Recommended Practices

> 来源: https://help.qsys.com/DeveloperHelp/#Recommended_Practices/TCP.htm

## TcpSocket Properties

### .ReadTimeout

- If socket receives no data within this time (seconds), it disconnects and calls Timeout EventHandler
- Value of 0 disables this behavior (default)
- After timeout, socket attempts reconnect if .ReconnectTimeout > 0
- **Should be greater than your poll rate** to prevent unwanted timeouts

### .WriteTimeout

- If socket sends no data within this time (seconds), it disconnects and calls Timeout EventHandler
- Value of 0 disables (default)
- After timeout, attempts reconnect if .ReconnectTimeout > 0
- Should be greater than your poll rate

### .ReconnectTimeout

- Time between reconnect attempts, in seconds
- Value of 0 disables reconnect
- **Default: 5 seconds**
- Socket with ReconnectTimeout > 0 continually tries to maintain connection until :Disconnect() is called

### .IsConnected

- Read-only, returns true if socket is connected
- Use to prevent calling :Write() when disconnected

```lua
function SendData(toSend)
  if socket.IsConnected then
    socket:Write(toSend)
  else
    print("Unable to send data, socket disconnected")
  end
end
```

### .BufferLength

- Read-only, returns buffer length in bytes
- Useful to determine if there is data to parse

## Socket Callbacks

| Callback | Description |
|----------|-------------|
| `.Connected` | Called when socket connects |
| `.Reconnect` | Called when socket reconnects |
| `.Closed` | Called when socket closes |
| `.Error` | Called on socket error |
| `.Timeout` | Called on read/write timeout |
| `.Data` | Called when data is received |

## Best Practices

1. Always check `.IsConnected` before writing
2. Set `.ReadTimeout` appropriately for your device's poll rate
3. Use `.ReconnectTimeout` for automatic reconnection
4. Print all socket events to debug for troubleshooting
5. Parse data in `.Data` callback using `socket:Read(socket.BufferLength)`
