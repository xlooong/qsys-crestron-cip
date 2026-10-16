# When

> 来源: https://help.qsys.com/q-sys_10.4/#Schematic_Library/when.htm

The When component enables you to schedule events based on specific days and times. Configure the component to activate events on selected days, at precise times, and for defined durations.

## Properties

This component does not have any configurable properties.

## Controls

| Control | Description |
|---------|-------------|
| Enable | Activates/deactivates the scheduled event. When disabled, event will not run. |
| Active LED | Indicates whether the scheduled event is currently active. |
| Days | Specify which days the event is allowed to run. All days enabled by default. |
| Time | Sets the exact time of day when the event should start. |
| Duration | How long the event remains active after start time. |

## Control Pins

| Pin Name | Type | Direction |
|----------|------|-----------|
| Enable | Boolean | Input/Output |
| Active | Boolean (LED) | Output |
| Day (Mon-Sun) | Boolean | Input/Output |
| Time | Text (HH:MM:SS) | Input/Output |
| Duration | Text | Input/Output |
