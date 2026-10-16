# Code Style Guide

> 来源: https://help.qsys.com/DeveloperHelp/#Standards_Definitions/Style_Guide.htm

## Formatting

### Naming

- **Branch Naming**: `main`, `develop`, `bugfix/MyBugFix`, `feature/MyNewFeature`
- **Controls, functions, aliases, global objects, global variables**: PascalCase / UpperCamelCase
- **Local variables and local objects**: camelCase / lowerCamelCase
- **Repository names (and plugin file names)**: PascalCase

### White Space

- One statement per line
- One assignment per statement
- Indentation: two spaces
- Space after control structures (if, for, while), operators, and commas

### Comments

- General comments (single or multi-line): one line above the respective chunk
- Granular comments: in line
- Section separators: single line comments with three asterisks: `--*** Section Name ***`

## Organization

### Design Time

1. General code info (plugin name, developer, date)
2. PluginInfo Header
3. Constants
4. Reserved functions
5. Custom functions needed during Design Time

### Runtime (within `if Controls then` conditional)

1. `require` declarations (alphabetically ordered)
2. Control Aliases
3. Variables
4. Objects and tables
5. Constants
6. Reserved function
7. Custom functions
8. EventHandlers
9. Initialization function
10. Print statements

### Socket Events

Always print to debug window for basic troubleshooting. Clear and concise format:
```
"Socket Closed due to error: [error message]"
```

## Example

```lua
-- An Example Plugin
-- by Your Name
-- Month Year

MyAlias = true
MyObject = {}

-- Basic commands
Commands = {
  NACK                = string.char(0x10),
  PingPong            = string.char(0x01),
  AnotherCommand      = string.char(0x20),
  AnEvenLongerCommand = string.char(0x21),
}

--*** Helper functions ***

-- This function is an example
function MyFunction()
  local myVariable
  if MyAlias then
    myVariable = false
  end
  return myVariable
end

-- This function is another example
function MyOtherFunction()
  local myString = "" -- A String
  if MyFunction() then
    myString = myString .. "Example"
  end
end
```
