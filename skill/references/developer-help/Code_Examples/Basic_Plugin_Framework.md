# Basic Plugin Framework

> 来源: https://help.qsys.com/DeveloperHelp/#Code_Examples/Basic_Plugin_Framework.htm

## Overview

A complete, minimal plugin framework showing all required and optional functions.

## Complete Example

```lua
-- Basic Plugin Framework Example
-- by QSC
-- 2024

PluginInfo = {
  Name = "Examples~Basic Plugin Framework",
  Version = "1.0.0",
  BuildVersion = "1.0.0",
  Id = "1a2b3c4d-5e6f-7a8b-9c0d-1e2f3a4b5c6d",
  Author = "QSC",
  Description = "An example plugin that demonstrates the basic plugin framework."
}

--*** Design Time Functions ***

-- Returns the name displayed on the component
function GetPrettyName(props)
  return "Basic Plugin Framework " .. PluginInfo.Version
end

-- Returns the component color {R, G, B}
function GetColor(props)
  return { 102, 102, 102 }
end

-- Defines user-configurable properties
function GetProperties()
  local props = {}
  table.insert(props, {
    Name = "Input Count",
    Type = "integer",
    Value = 2,
    Min = 1,
    Max = 8
  })
  table.insert(props, {
    Name = "Enable Debug",
    Type = "boolean",
    Value = false
  })
  return props
end

-- Runs after property changes; adjust visibility/globals
function RectifyProperties(props)
  return props
end

-- Defines pages (optional)
function GetPages(props)
  return { { name = "Main" } }
end

-- Defines controls
function GetControls(props)
  local ctrls = {}
  table.insert(ctrls, {
    Name = "MyButton",
    ControlType = "Button",
    ButtonType = "Toggle",
    UserPin = true,
    PinStyle = "Input",
    Count = 1
  })
  table.insert(ctrls, {
    Name = "MyKnob",
    ControlType = "Knob",
    ControlUnit = "Integer",
    Min = 0,
    Max = 100,
    UserPin = true,
    PinStyle = "Input",
    Count = 1
  })
  table.insert(ctrls, {
    Name = "MyText",
    ControlType = "Text",
    UserPin = true,
    PinStyle = "Output",
    Count = 1
  })
  return ctrls
end

-- Defines panel layout; returns (layout, graphics)
function GetControlLayout(props)
  local layout = {}
  local graphics = {}

  layout["MyButton"] = {
    PrettyName = "My Button",
    Style = "Toggle",
    Position = { 10, 10 },
    Size = { 80, 30 }
  }
  layout["MyKnob"] = {
    PrettyName = "My Knob",
    Style = "Knob",
    Position = { 10, 50 },
    Size = { 80, 40 }
  }
  layout["MyText"] = {
    PrettyName = "My Text",
    Style = "Text Display",
    Position = { 10, 100 },
    Size = { 150, 30 }
  }

  table.insert(graphics, {
    Type = "GroupBox",
    Text = "Controls",
    Position = { 0, 0 },
    Size = { 200, 150 },
    StrokeWidth = 1,
    StrokeColor = { 51, 51, 51 },
    CornerRadius = 8,
    FontSize = 14,
    HTextAlign = "Left"
  })

  return layout, graphics
end

--*** Runtime ***

if Controls then
  -- Aliases
  MyButton = Controls.MyButton
  MyKnob = Controls.MyKnob
  MyText = Controls.MyText

  -- Variables
  lastKnobValue = 0

  -- Functions
  function UpdateText()
    MyText.String = string.format("Button: %s, Knob: %d",
      tostring(MyButton.Boolean), MyKnob.Value)
  end

  -- Event Handlers
  MyButton.EventHandler = function()
    UpdateText()
  end

  MyKnob.EventHandler = function()
    UpdateText()
  end

  -- Initialization
  print("Basic Plugin Framework " .. PluginInfo.Version .. " started")
  UpdateText()
end
```

## Key Points

1. **PluginInfo** must include Name, Version, Id (unique GUID)
2. **GetProperties()** returns property table
3. **GetControls()** returns control definitions
4. **GetControlLayout()** returns (layout, graphics)
5. Runtime code wrapped in `if Controls then ... end`
6. Print version at start of runtime for debugging
