# SerialPorts

> 来源: https://help.qsys.com/q-sys_10.4/#Control_Scripting/Using_Lua_in_Q-Sys/SerialPorts.htm

Serial port communication is supported via the RS-232 ports on some Q-SYS devices. You can use a scripting component, including Control Script and Block Controller, to create a serial port connection in Q-SYS.

The following content describes creating a serial connection with the Control Script component. To see an example of creating a serial connection with the Block Controller component, see Block Examples.

## Creating a Serial Connection with Control Script

To access serial communications, Serial Inputs must be enabled (not 0) in the Control Script's Properties. The Q-SYS device's Serial Port component is then dragged into the design's schematic and wired to the Control Script. In the script itself, there is no 'New' SerialPort method because SerialPort objects are automatically created for you whenever a Q-SYS device's serial port Inventory component is wired into the ControlScript block.

Note: Serial functionality is only available when deployed to a Q-SYS Core and is not available via emulation like many other Q-SYS Lua extensions.

## Callbacks
Optional callback func
