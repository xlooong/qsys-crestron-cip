# EzSVG

> 来源: https://help.qsys.com/q-sys_10.4/#Control_Scripting/Using_Lua_in_Q-Sys/EzSVG.htm

Use the EzSVG library to create SVG images dynamically within your design - for example, to help users visualize component status and control level changes.

Note: Additional documentation can be found on the EzSVG page on Github within its README markdown file.

## Syntax

Q-SYS implements the EzSVG library in its entirety with one addition and exception:

Use **toString()** as a replacement for the standard writeTo() call to ensure that the encoded SVG document is returned as a string.

## Examples
- Inventory pie chart
- Generic pie chart
- Live audio graph

All examples use a Text Controller component for scripting, and each SVG graphic (called a "document") is drawn to a toggle button control.
