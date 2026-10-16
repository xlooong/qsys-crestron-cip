# Plugin Property Headers and Comments

> 来源: https://help.qsys.com/DeveloperHelp/#Code_Examples/Plugin_Property_Headers_Comments.htm
> 要求: Q-SYS Designer v9.10+

## Overview

Starting in Q-SYS Designer v9.10, you can define Headers and Comments for properties:
- **Headers**: Group similar/related properties under a single Header
- **Comments**: Convey relevant info (default value, accepted range) to end user

## Example Code

```lua
function GetProperties()
  local props = {}
  table.insert(props, {
    Name = "Input Count",
    Type = "integer",
    Value = 8,
    Min = 2,
    Max = 32,
    Comment = "Range: 2-32"
  })
  table.insert(props, {
    Name = "Output Count",
    Type = "integer",
    Value = 8,
    Min = 1,
    Max = 32,
    Comment = "Range: 1-32"
  })
  table.insert(props, {
    Name = "Type",
    Type = "enum",
    Value = "Mono",
    Choices = {"Mono", "Stereo", "Multi-channel"},
    Header = "Channels"
  })
  table.insert(props, {
    Name = "Count",
    Type = "integer",
    Value = 8,
    Min = 2,
    Max = 64,
    Comment = "Range: 2-64",
    Header = "Channels"
  })
  return props
end

function RectifyProperties(props)
  props["Count"].IsHidden = (props["Type"].Value ~= "Multi-channel")
  return props
end
```

## Property Fields

| Field | Type | Description |
|-------|------|-------------|
| Name | String | Property name displayed in Properties pane |
| Type | String | "string", "integer", "double", "boolean", "enum" |
| Value | Varies | Default value |
| Choices | Table | Choice strings for "enum" type |
| Min | Integer | Minimum for integer/double |
| Max | Integer | Maximum for integer/double |
| Header | String | Group header (v9.10+) |
| Comment | String | Comment shown below property (v9.10+) |
| IsHidden | Boolean | Set in RectifyProperties to hide/show |
