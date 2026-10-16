# SNMPTrap

> 来源: https://help.qsys.com/q-sys_10.4/#Control_Scripting/Using_Lua_in_Q-Sys/SNMPTrap.htm

Use the SNMPTrap library in Lua to receive trap notifications from an SNMP-enabled device.

Note: In the SNMP model, Q-SYS acts as the SNMP Manager, while the device you intend to monitor runs an SNMP Agent that allows for monitoring.

## Methods

| Method | Description |
|--------|-------------|
| SNMPTrap.New | Create a new SNMP trap listener. |
| startSession | Begin a trap listening session. |
| EventHandler | Assign a Lua callback for successful SNMP events. |
| ErrorHandler | Assign a Lua callback for unsuccessful SNMP events. |
