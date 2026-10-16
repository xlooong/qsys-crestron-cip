# NamedControl

> 来源: https://help.qsys.com/q-sys_10.4/#Control_Scripting/Using_Lua_in_Q-Sys/NamedControl.htm

The methods in NamedControl are used to read or set the values of Named Controls.

## Methods

| Method | Arguments | Description |
|--------|-----------|-------------|
| .SetString | Control name, string | Class static. Sets control with specified Control name to specified string value. If Control name does not exist an error is raised. |
| .GetString | Control name | Class static. Returns string of control with specified Control name. If Control name does not exist an error is raised. |
| .SetPosition | Control name, position, optional ramp time | Class static. Sets control with specified Control name to specified position. The ramp time is optional, and is in seconds. |
| .GetPosition | Control name | Class static. Returns position of control with specified Control name. |
| .SetValue | Control name, value, optional ramp time | Class static. Sets control with specified Control name to specified value. The ramp time is optional, and is in seconds. |
