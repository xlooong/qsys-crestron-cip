# Network

> 来源: https://help.qsys.com/q-sys_10.4/#Control_Scripting/Using_Lua_in_Q-Sys/Network.htm

Use the Network commands to return the full host name and IP address of a specified host, or obtain a table of network interface names and their IP addresses.

## Methods

### Network.GetHostByName
Return an object with the name (.name) and addresses (.addresses) of a specified host, where .addresses is a table of strings.

### Network.Interfaces
Return a table of network interface names (.Interface) and the IP address (.Address), MAC address (.MACAddress), broadcast address (.BroadcastAddress), gateway (.Gateway), and netmask (.Netmask) for each.
