# LuaXML

> 来源: https://help.qsys.com/q-sys_10.4/#Control_Scripting/Using_Lua_in_Q-Sys/LuaXML.htm

Using the LuaXML module provides a very simple and natural mapping between the XML data format and Lua tables. Allowing you to parse XML data just using Lua's normal table access and iteration methods.

## Methods

| Method | Description |
|--------|-------------|
| xml.new() | Creates a new LuaXML object. |
| xml.append() | Appends a new subordinate LuaXML object to an existing one, optionally sets tag. |
| xml.children() | Iterate subelements ("XML children") as key-value pairs. |
| xml.decode() | Converts a string from XML encoding. |
| xml.encode() | Converts a string to XML encoding. |
| xml.interate() | Iterates a LuaXML object, invoking a callback function for all matching (sub)elements. |
| xml.match() | Match XML entity against given (optional) criteria. |
| xml.load() | Loads XML data from a file and returns it as table. |
| xml.save() | Saves a Lua var as XML file. |
| xml.eval() | Converts an XML string to a Lua table. |
| xml.tag() | Sets or returns tag of a LuaXML object. |
| xml.str() | Converts any Lua var to an xml string. |
| xml.find() | Recursively parses a Lua table for a substatement fitting to the provided criteria. |
