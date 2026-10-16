# Flip-Flop

> 来源: https://help.qsys.com/q-sys_10.4/#Schematic_Library/flip_flop.htm

The Flip-Flop Component converts a trigger type input to a Boolean type output.

## Use Cases

### Use Case 1 - Momentary button as toggle
- Wire momentary button to Toggle Input → each press changes State

### Use Case 2 - Separate ON/OFF buttons
- Wire ON button to Set Input, OFF button to Reset Input
- Press ON → Set (State may change)
- Press OFF → Reset (State may change)

## Control Pins

| Pin Name | Type | Direction | Description |
|----------|------|-----------|-------------|
| Set | Trigger | Input | Sets output to true |
| Reset | Trigger | Input | Sets output to false |
| Toggle | Trigger | Input | Toggles output state |
| State | Boolean | Output | Current flip-flop state |
