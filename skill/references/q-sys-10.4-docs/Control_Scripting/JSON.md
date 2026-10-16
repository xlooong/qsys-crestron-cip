# JSON

> 来源: https://help.qsys.com/q-sys_10.4/#Control_Scripting/Using_Lua_in_Q-Sys/JSON.htm

Use the JSON module to encode and decode Lua tables to and from JSON strings.

Note: For faster performance, and to avoid raising execution count errors with large amounts of data, use RapidJSON instead.

To use the JSON module, add the following line to your script:
```lua
require("json")
```

## Methods

### json.encode()
Returns the Lua object JSON encoded into a string.

### json.decode()
Decodes the JSON encoded data structure, and returns a Lua object with the appropriate data.

### json.null()
Returns a unique value that will be encoded as a null in a JSON encoding.

Portions of this topic are reprinted under permission of the JSON4Lua license.
