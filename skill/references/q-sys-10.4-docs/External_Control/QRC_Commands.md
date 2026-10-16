# QRC Commands - Q-SYS Remote Control Protocol

> 来源: https://help.qsys.com/q-sys_10.4/#External_Control_APIs/QRC/QRC_Commands.htm
> 端口: 1710 | 协议: JSON RPC 2.0, null-terminated

QRC is a Unicode-based TCP/IP control protocol. The client connects to the Q-SYS Core (or emulator) on port 1710 and sends JSON RPC 2.0 null-terminated commands.

**Tip**: In all QRC commands, `id` acts as an identifier and allows for the sender to match the response with the command. The id field must be a number.

## Formatting Requirements

Every QRC command must:
1. Be a command from the supported commands listed below
2. Be terminated in a null character (`\0`)

---

## Connection Methods

### Logon
Logs on to the system. User credentials must first be created in Users (Administrator).

**Parameters**: User, Password

```json
{
  "jsonrpc":"2.0",
  "method":"Logon",
  "params":{
    "User":"username",
    "Password":"1234"
  }
}
```

### NoOp
A simple "do nothing" method for making sure that the socket remains open.

```json
{
  "jsonrpc":"2.0",
  "method":"NoOp",
  "params":{}
}
```

---

## Status Methods

### StatusGet
Manually request the current status. Returns the EngineStatus of the Q-SYS Core.

**Response Results**:
- **Platform**: The Q-SYS Core model
- **State**: "Idle", "Active", or "Standby"
- **DesignName**: Name of the currently running design
- **DesignCode**: GUID of the currently running design
- **IsRedundant**: True if redundant design
- **IsEmulator**: True if running in emulator

```json
{
  "jsonrpc": "2.0",
  "method": "StatusGet",
  "id": 1234,
  "params": 0
}
```

---

## Control Methods (Named Controls)

### Control.Get
Specify an array of Named Control strings, receive an array of control values.

**Parameters**: Array of Named Control strings

**Response**: Name, Value (number/string/boolean), String

```json
{
  "jsonrpc": "2.0",
  "id": 1234,
  "method": "Control.Get",
  "params": ["MainGain", "MainMute"]
}
```

### Control.Set
Set a control's value. Specify a single control name, value, and optional ramp time.

**Parameters**: Name, Value, Ramp (optional)

```json
{
  "jsonrpc": "2.0",
  "id": 1234,
  "method": "Control.Set",
  "params": {
    "Name": "MainGain",
    "Value": -12
  }
}
```

---

## Component Control Methods

### Component.Get
Returns the values of one or more specified controls within a specified Named Component.

**Parameters**: Name (component), Controls (array of control names)

```json
{
  "jsonrpc": "2.0",
  "id": 1234,
  "method": "Component.Get",
  "params": {
    "Name": "My APM",
    "Controls": [{ "Name": "ent.xfade.gain" }]
  }
}
```

### Component.GetControls
Returns a table of all controls and their values in a specified Named Component.

**Parameters**: Name (component)

Response includes: Name, Type (Boolean/Float/etc), Value, ValueMin, ValueMax, String, Position, Direction (Read/Write)

### Component.Set
Set one or more controls for a single named component. Returns a list of unknown controls after processing.

**Parameters**: Name, Controls (array), ResponseValues (optional boolean)

```json
{
  "jsonrpc": "2.0",
  "id": 1234,
  "method": "Component.Set",
  "params": {
    "Name": "My APM",
    "Controls": [
      { "Name": "ent.xfade.gain", "Value": -100.0, "Ramp": 2.0 }
    ]
  }
}
```

### Component.GetComponents
Get a list of all named components in a design, along with their type and properties.

Response fields: Name, ID, Type, Properties (design-time properties, read-only), ControlSource

---

## Change Group Methods

> Note: Maximum of 4 change groups, no restriction on number of controls within a group.

### ChangeGroup.AddControl
Create a change group and/or add controls via Named Controls.

**Parameters**: Id, Controls (array)

### ChangeGroup.AddComponentControl
Create a change group and/or add controls via a Named Component.

**Parameters**: Id, Component (Name + Controls array)

### ChangeGroup.Remove
Remove controls from a change group via Named Controls.

### ChangeGroup.Poll
Poll a change group. Returns changes since last poll.

```json
{
  "jsonrpc": "2.0",
  "id": 1234,
  "method": "ChangeGroup.Poll",
  "params": { "Id": "my change group" }
}
```

### ChangeGroup.Destroy
Destroy a change group.

### ChangeGroup.Invalidate
Invalidates a change group, causing all controls to be resent.

### ChangeGroup.Clear
Clears a change group, removing all controls.

### ChangeGroup.AutoPoll
Set up automatic polling at a specified interval.

**Parameters**: Id, Rate (seconds)

---

## Mixer Control Methods

Uses string specification for inputs/outputs: `*` (all), `1 2 3`, `1-6`, `1-6 9`, `1-8 !3`, `* !3-5`

### Methods
- **Mixer.SetCrossPointGain** (Name, Inputs, Outputs, Value, Ramp)
- **Mixer.SetCrossPointDelay** (Name, Inputs, Outputs, Value, Ramp)
- **Mixer.SetCrossPointMute** (Name, Inputs, Outputs, Value)
- **Mixer.SetCrossPointSolo** (Name, Inputs, Outputs, Value)
- **Mixer.SetInputGain** (Name, Inputs, Value, Ramp)
- **Mixer.SetInputMute** (Name, Inputs, Value)
- **Mixer.SetInputSolo** (Name, Inputs, Value)
- **Mixer.SetOutputGain** (Name, Outputs, Value, Ramp)
- **Mixer.SetOutputMute** (Name, Outputs, Value)
- **Mixer.SetCueMute** (Name, Cues, Value)
- **Mixer.SetCueGain** (Name, Cues, Value, Ramp)
- **Mixer.SetInputCueEnable** (Name, Cues, Inputs, Value)
- **Mixer.SetInputCueAfl** (Name, Cues, Inputs, Value)

---

## Loop Player Control Methods

> Note: All Loop Player commands have a Log option (true/false) for Event Log logging.

### LoopPlayer.Start
Schedules one or more file playback assignments.

**Parameters**:
- Name (required): Loop Player component Code Name
- StartTime: -1=immediately, -2=queue at end, 0+=absolute time-of-day (UTC seconds)
- Files (required array): Name (path), Output (required), Loop, Log, RefID, Seek

### LoopPlayer.Stop
Stops playback on specified output tracks. Parameters: Name, Outputs, Log, RefID

### LoopPlayer.Cancel
Cancels pending/queued playback without disrupting current playback. Parameters: Name, Outputs, Log, RefID

---

## Snapshot Methods

### Snapshot.Load
Load control settings from a snapshot bank and number with optional ramp time.

**Parameters**: Name (bank name), Bank (1-N), Ramp (optional seconds)

```json
{
  "jsonrpc": "2.0",
  "method": "Snapshot.Load",
  "params": { "Name": "MySpecialBank", "Bank": 7, "Ramp": 8.5 },
  "id": 1234
}
```

### Snapshot.Save
Save control settings to a snapshot bank and number.

**Parameters**: Name, Bank

---

## Error Code Reference

| Code | Details |
|------|---------|
| -32700 | Parse error. Invalid JSON |
| -32600 | Invalid request |
| -32601 | Method not found |
| -32602 | Invalid params |
| -32603 | Server error |
| -32604 | Core is on Standby |
| 2 | Invalid Page Request ID |
| 3 | Bad Page Request |
| 4 | Missing file |
| 5 | Change Groups exhausted |
| 6 | Unknown change group |
| 7 | Unknown component name |
| 8 | Unknown control |
| 9 | Illegal mixer channel index |
| 10 | Logon required |
