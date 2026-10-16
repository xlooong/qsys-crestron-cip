# Timer

> 来源: https://help.qsys.com/q-sys_10.4/#Control_Scripting/Using_Lua_in_Q-Sys/Timer.htm

The Timer object is used to create delays or trigger events after a defined elapsed time. It should be used instead of Lua's native delay and time functions.

## Methods

### Timer.New()
Creates a named timer using Start and Stop methods.

### Timer.CallAfter()
Creates a simple timer that calls a named function after a specified delay time.

### Timer.Now()
Returns the number of seconds since epoch.

## Troubleshooting
