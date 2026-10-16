# Ping

> 来源: https://help.qsys.com/q-sys_10.4/#Control_Scripting/Using_Lua_in_Q-Sys/Ping.htm

Use the Ping library in Lua to check whether a device is reachable on the network.

Note: The Lua Ping library requires that you run Q-SYS Designer as administrator when emulating your design. If you see a non-terminating "Socket failed to open" error message in the debug window, re-launch Designer as administrator.

## Methods

| Method | Description |
|--------|-------------|
| Ping.New | Create a new ping object. |
| start | Begin the ping session. |
| stop | Stop the ping session. |
| setTimeoutInterval | Set the timeout for waiting for a ping response. |
| setPingInterval | Set the interval for retrying after a ping request. |
| EventHandler | Assign a Lua callback for successful ping events. |
| ErrorHandler | Assign a Lua callback for unsuccessful ping events. |
