# Plugin Debug Methods

> 来源: https://help.qsys.com/DeveloperHelp/#Recommended_Practices/Plugin_Debug.htm

## Debug Recommendations

### Script Start

Print `PluginInfo.Version` to debug at start of runtime.

### Functions

- Function calls should be printed, may include arguments
- Utility functions that may spam debug should only print during development or with an explicit enable/disable flag

### Connection State

Connection state events should be printed with relevant error statements:
- Connected
- Disconnected
- Closed
- Error
- Timeout
- Reconnect

### Data Logging

There should be a way to print incoming data, outgoing data, or both, to debug. May be enabled via a property or control. Data should be formatted to assist users and support:
- Convert bytes to decimal or hexadecimal strings
- Use `hex2str()` helper for binary data

### File Operations

File operations should have debug logging (writes, reads, deletes, directory addition/removal). May be enabled via property or control.

Updates to log files don't need printing, but creation/deletion of log files must be printed.

### Inter-Plugin Communication

Should have debug logging, enabled via property or control.

## Debug Methods

### Print Statements (Recommended)

Simplest method. Minimum requirements:
- Print `PluginInfo.Version`
- Print connection status changes
- Print errors

### Show Debug Property

All plugins automatically get a "Show Debug" property with default value "No". When set to "Yes", users can see the debug print window.

## Debug Pattern

```lua
-- At start of runtime
print("My Plugin " .. PluginInfo.Version .. " started")

-- Socket events
socket.Connected = function()
  print("[TCP] Connected to " .. IPAddress.String)
end

socket.Closed = function()
  print("[TCP] Connection closed")
end

socket.Error = function()
  print("[TCP] Socket error")
end

-- Data logging (with debug flag)
if Properties["Enable Debug"].Value then
  print("[RX] " .. hex2str(data))
end
```
