# Lua bitstring

> 来源: https://help.qsys.com/q-sys_10.4/#Control_Scripting/Using_Lua_in_Q-Sys/Lua_bitstring.htm

Bitstring is useful for network protocol programming and for manipulation of bit based file formats. It provides conversion of strings to binary and hexadecimal formats.

## Methods

| Method | Description |
|--------|-------------|
| bitstring.pack() | Pack one or more elements as specified by format or by bitmatch into regular Lua string. |
| bitstring.unpack() | Unpack one or more elements as specified by format or by bitmatch and return them as multiple values. |
| bitstring.compile() | Compiles format into bitmatch object. |
| bitstring.bindump() | Dump string into multi line "offset - binary digits - text" similar to xxd -b output. |
| bitstring.hexdump() | Dumps string into multi line, similar to xxd output. |
| bitstring.binstream() | Dumps string into single line binary digit stream. |
| bitstring.hexstream() | Dumps string into single line hexadecimal digit stream. |
| bitstring.frombinstream() | Convert hexadecimal stream of bytes to regular Lua string. |
| bitstring.fromhexstream() | Convert hexadecimal stream of bytes to regular Lua string. |

## Sections
- Usage
- Substring Parameters
- Format Specification

Portions of this topic are reprinted under permission of the bitstring license.
