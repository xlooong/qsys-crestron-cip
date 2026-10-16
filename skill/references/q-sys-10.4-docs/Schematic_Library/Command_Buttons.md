# Command Buttons

> 来源: https://help.qsys.com/q-sys_10.4/#Schematic_Library/command_buttons.htm

The Command Buttons component gives you up to 64 buttons to which you can assign a command string that is sent when the button is pressed. You can send the commands via TCP, UDP, or Serial (RS-232).

## Properties

| Property | Description |
|----------|-------------|
| Type | Communication method: TCP (default), UDP, or Serial |
| Command Count | Number of command lines, 1 to 64 (default 8) |

## Controls

- **Status**: OK(0), Compromised(1), Fault(2), Not Present(3), Unknown(3), Missing(4), Initializing(5)
- **IP Address, Port**: For TCP/UDP only. Default port 80. IP field only accepts IP addresses, not host names.
- **Config (Serial only)**: Baud Rate (50-230400, default 9600), Data Bits (7/8, default 8), Parity (None/Odd/Even, default None), Stop Bits (1/2, default 1)
- **Command String**: Enter the command string.

### Sending hex strings
Insert `\x` before each pair. Example: `01 2f 00 01 01` + CR = `\x01\x2f\x00\x01\x01\x0d`
- Carriage return: `\x0d` or `\r`
- Line feed: `\x0a` or `\n`

- **Command n Trigger**: Click to send the command.

## Control Pins

| Pin Name | Value | String | Position | Direction |
|----------|-------|--------|----------|-----------|
| Status | (text) | — | — | Output |
| Command n | — | (text) | — | Input/Output |
| Trigger | (trigger) | — | — | Input/Output |
| IP Address | — | (text) | — | Input/Output |
| Port | 0 to 100000 | text | — | Input/Output |
| Baud Rate | 50 to 230400 | text | — | Input/Output |
| Data Bits | 7 or 8 | 7 or 8 | — | Input/Output |
| Parity | None, Odd, Even | — | — | Input/Output |
| Stop Bits | 1 or 2 | 1 or 2 | — | Input/Output |
