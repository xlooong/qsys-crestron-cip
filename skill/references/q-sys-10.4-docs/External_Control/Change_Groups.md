# Change Groups for ECP and QRC

> 来源: https://help.qsys.com/q-sys_10.4/#External_Control_APIs/external_controls_change_groups.htm

Q-SYS provides monitoring capability through the use of Change Groups. A Change Group is a grouping of controls, created by your code, that is polled at a schedule interval. When the Change Group is polled, it returns the state of any controls that have changed since the last polling.

## Change Group Requirements

Q-SYS operates on a client-server basis. The Q-SYS Core is the server, the external control system is the client. A Core must have a design loaded and in Run mode for an external system to connect to it.

When a control is added to an existing Change Group, it is considered changed so the Core responds with the new control's state even if it has not changed.

## Change Group Limits

The maximum number of simultaneous Change Groups is **512**.

| Client | Change Groups Used |
|--------|-------------------|
| Q-SYS Designer Instance | 1 |
| Active iOS UCI | 1 |
| Active UCI Instance (TSC, UCI Viewer) | 1 each |
| Core 110 or 3100 | 2 |
| Redundant Core (redundant networking) | 2 |
| Redundant Core (non-redundant networking) | 1 |
| External Control System | 0-4 |

Note: If the maximum number of Change Groups (512) is reached, scripts will output a "Too many change groups" debug message.

## Lua Script Change Group Behavior

Each Lua script component that assigns an EventHandler on a component control (e.g., controls accessed via Component.New) consumes one Change Group. The Change Group is created only when the first EventHandler is assigned. A script that only reads or writes control values without setting an EventHandler does not consume a Change Group. Multiple EventHandlers within the same script component still only use one Change Group slot.

Note: Assigning EventHandlers to Controls.Inputs[n] or Controls.Outputs[n], which are built-in controls, does not create a Change Group, as these controls use the observer pattern instead.
