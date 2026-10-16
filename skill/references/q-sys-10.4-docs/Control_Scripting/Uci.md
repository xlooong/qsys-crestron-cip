# Uci

> 来源: https://help.qsys.com/q-sys_10.4/#Control_Scripting/Using_Lua_in_Q-Sys/Uci.htm

Use the Uci API functions to programmatically control and modify user control interfaces in Q-SYS.

## UCI Script Overview

The UCI Script tab contains a familiar interface for authoring Lua code specific to the selected UCI. This makes it easy to duplicate a UCI and update the new one (i.e., modify the script) with different parameters.

Note: Some Lua methods are not supported. When referencing the Uci Lua methods in your UCI script, it will not work if you define the UCI_Name variable because the script is local to the UCI and its name.

## Uci.Get Methods

| Method | Description |
|--------|-------------|
| Uci.GetLayerVisibility | If no argument is specified, returns a table of UCI, page, layer names, and layer visibility status. |
| Uci.GetUcis | Returns an array of UCI name tables. |
| Uci.GetUciPages | Returns an array of UCI page name tables in a specified UCI. |
| Uci.GetUciPageLayers | Returns an array of UCI page layer name tables in a specified UCI. |
| Uci.GetVariable | Retrieves the value of a variable that has been set in the UCI. |

## Uci.LogOff Methods
Uci.LogOff - Enable the ability to log off from a specified UCI.
