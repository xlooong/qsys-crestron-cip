# RapidJSON

> 来源: https://help.qsys.com/q-sys_10.4/#Control_Scripting/Using_Lua_in_Q-Sys/RapidJSON.htm

Use the RapidJSON module to quickly encode and decode large Lua tables to and from JSON documents (strings). This may be useful in cases where an API is expecting a JSON string (instead of tables), or if you want to convert a Lua table of values into a string that can then be saved in a control value.

Tip: RapidJSON is similar to the standard JSON module, but can handle large amounts of data without risk of raising execution count errors. For this reason, it is recommended to use the RapidJSON module instead of the JSON module.

## Usage

### Name and Version
Returns the RapidJSON name or version.

### rapidjson.encode()
Encode a Lua table to JSON string. JSON object keys are sorted by this function.

### rapidjson.decode()
Decode JSON to a Lua table.

### rapidjson.load()
Load JSON file into Lua table.

### rapidjson.Document()
Creates a rapidjson Document object. Optionally create from a Lua table or string of JSON document.

### document:parse()
Parse JSON document contained in string s.

### document:get()
Get document member by JSON Pointer.

### document:set()
Set document member by JSON Pointer with specified value.

### rapidjson.dump()
Dump a Lua value to a JSON file.

### rapidjson.null
The placeholder for null values in rapidjson.

### rapidjson.object()
Create a new empty table that has the metatable field __jsontype set as 'object' so that the encode and dump function will encode it as a JSON object.
