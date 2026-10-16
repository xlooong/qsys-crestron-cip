# Mixer

> 来源: https://help.qsys.com/q-sys_10.4/#Control_Scripting/Using_Lua_in_Q-Sys/Mixer.htm

Mixer objects allow access to Mixer components that have been named in the design. To create a mixer object, call Mixer.New(mixerName). The mixer object uses a string specification to determine which inputs and outputs to apply changes to. The syntax supports either space or comma separated numbers, ranges of numbers or all (*). It supports negation of selection with the '!' operator.

## Input/Output String Specification

| Spec | Description |
|------|-------------|
| * | Everything |
| 1 2 3 | channels 1, 2, 3 |
| 1-6 | channels 1 through 6 |
| 1-6 9 | channels 1 through 6 and 9 |
| 1-3 5-9 | channels 1 through 3 and 5 through 9 |
| 1-8 !3 | channels 1 through 8 except 3 |
| * !3-5 | everything but channels 3 through 5 |

## Mixer Methods

| Method | Arguments | Description |
|--------|-----------|-------------|
| SetCrossPointGain | (ins, outs, gain, ramp) | Sets specified cross point gains with optional ramp time. |
| SetCrossPointMute | (ins, outs, mute) | Sets specified cross point mutes with boolean |
| SetCrossPointSolo | (ins, outs, mute) | Sets specified cross point solos with boolean |
| SetCrossPointDelay | (ins, outs, delay, ramp) | Sets specified cross point delay with optional ramp time |
| SetInputGain | (ins, gain, ramp) | Sets specified input gain with optional ramp time |
| SetInputMute | (ins, mute) | Sets specified input mutes |
| SetInputSolo | (ins, solo) | Sets specified input solos |
