# Handling Hex and Binary Data

> 来源: https://help.qsys.com/DeveloperHelp/#Code_Examples/Hex_Data_Handling.htm

## Overview

Received data from TCPSocket, UDPSocket, and Serial objects is formatted as ASCII characters wrapped in a string. Each character represents one byte (0-255 decimal).

## Byte Encoding Equivalences

```
"\x41" == "\65" == "A" = string.char(65) == string.char(0x41)
0x41 == 65 == string.byte("A")
```

## Helper Functions

```lua
-- Convert string bytes to human-readable hex pairs
function hex2str(str)
  return str:gsub(".", function(byte)
    return string.format("%02X", string.byte(byte))
  end)
end

-- Convert hex pairs string to character-encoded bytes
function str2hex(str)
  return str:gsub("..", function(byte)
    return string.char(tonumber(byte, 16))
  end)
end

-- Return numerical equivalent of bytes (max 7 bytes before overflow)
function hex2num(str)
  local value = 0
  if str:len() > 0 then
    for i = 1, str:len() do
      value = str:byte(i) + (value << 8)
    end
  end
  return value
end

-- Return string of bytes equivalent to numerical value
function num2hex(val)
  local str = ""
  while val > 0 do
    str = string.char(val % 256) .. str
    val = val >> 8
  end
  return str
end
```

## Bitwise Operators

- `&` bitwise AND
- `|` bitwise OR
- `~` bitwise exclusive OR
- `>>` right shift
- `<<` left shift
- `~` unary bitwise NOT

## Escape Character Encoding from Q-SYS Text Inputs

Q-SYS text inputs encode user input with escape characters. Supported: `\x??` hex, `\###` decimal, `\a`, `\b`, `\f`, `\r`, `\n`, `\t`, `\v`.

```lua
function EscapeSequenceEncode(str)
  -- Converts escape sequences to actual characters
  -- Supports \x?? hex, \### decimal, \a \b \f \r \n \t \v
end
```

## Test Examples

```lua
local data = "\x48\x65\x6C\x6C\x6F\x20\x57\x6F\x72\x6C\x64\x21"
print(data)           --> Hello World!
data = hex2str(data)
print(data)           --> 48656C6C6F20576F726C6421
print(str2hex(data))  --> Hello World!

data = "\xDE\xCA\xFB\xAD"
print(hex2str(data))  --> DECAFBAD
data = hex2num(data)
print(data)           --> 3737844653
data = num2hex(data)
print(hex2str(data))  --> DECAFBAD
```
