# Component

> 来源: https://help.qsys.com/q-sys_10.4/#Control_Scripting/Using_Lua_in_Q-Sys/Component.htm

Component objects allow access to Named Components in the design. To create a Named Component, enable Code Name and Script Access for the component block.

Note: The Code Name and Script Access feature takes the place of typing a name on a Component in previous versions of Q-SYS Designer. While it is not expected to affect existing designs, it is possible that adjustments may be needed to some scripts and/or Code Names.

## Methods

### Component.New()
Create a Named Component reference in your script.

### Component.GetComponents()
Returns a Lua table describing all Named Components in the design and their properties.

- With no arguments, returns a table of all Named Components.
- With a string argument, returns a table containing only the Named Component with that Code Name, if it exists.

Each entry in the returned table is itself a table that describes one Named Component.

The table contains the following fields:

- **Name**: The Code Name of the Named Component.
- **ID**: This also contains the Code Name of the Named Components returned by Component.GetComponents(), Name and ID are in this context, identical.
- **Type**: A string that identifies the component's class / type. Instances of the same component class share the same Type value.
