# SNMP

> 来源: https://help.qsys.com/q-sys_10.4/#Control_Scripting/Using_Lua_in_Q-Sys/SNMP.htm

Use the SNMP library in Lua to monitor OIDs obtained from an SNMP-enabled device's MIB file.

Note: In the SNMP model, Q-SYS acts as the SNMP Manager, while the device you intend to monitor runs an SNMP Agent that allows for monitoring.

## Methods

| Method | Description |
|--------|-------------|
| SNMPSession.New | Create a new SNMP session. |
| setHostName | Specify the host to which to connect. |
| setAuthType | For SNMP v3 only, set the authorization type. |
| setAuthProt | For SNMP v3 only, set the authorization protocol. |
| setPrivProt | For SNMP v3 only, set the privacy protocol. |
| setUserName | For SNMP v3 only, set the user name. |
| setPassPhrase | For SNMP v3 only, set the authorization pass phrase. |
| setPrivPassPhrase | For SNMP v3 only, set the privacy pass phrase. |
| setCommunity | For SNMP v2 sessions only, set the community name. |
| startSession | Initiate the connection to the corresponding session. |
| getRequest | Request an object ID (OID) and pass the response to a Lua callback. |
| setRequest | Set a new value for a specified OID. |
| EventHandler | Assign the Lua callback for successful SNMP events. |
| ErrorHandler | Assign the Lua callback for unsuccessful SNMP events. |
