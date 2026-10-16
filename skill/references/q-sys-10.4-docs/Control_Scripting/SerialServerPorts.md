# SerialServerPorts

> 来源: https://help.qsys.com/q-sys_10.4/#Control_Scripting/Using_Lua_in_Q-Sys/SerialServerPorts.htm

Use the SerialServerPorts library to emulate the functionality of Q-SYS hardware Serial Port components, while internally redirecting connection state and data bidirectionally to and from a remote serial server device. SerialServerPorts allows you to bridge the gap between serial wiring and Lua TcpSocket library paradigms.

If you already have a script that successfully interfaces with RS-232-controlled gear using native Q-SYS serial ports, it can now be wired to a Virtual Serial Port, which establishes a communication path to a remote networked device port.

Note: To use the SerialServerPorts library in a Lua script, you must expose Virtual Serial Ports in a supported Q-SYS scripting component: Text Controller or Control Script.

## Sections
- Properties
- Methods
- SerialServerPorts Callbacks
- SerialPorts.Events Table
- SerialPorts.EOL Table
- Example
