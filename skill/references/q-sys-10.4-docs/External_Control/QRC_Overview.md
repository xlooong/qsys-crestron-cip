# Q-SYS Remote Control Protocol (QRC) Overview

> 来源: https://help.qsys.com/q-sys_10.4/#External_Control_APIs/QRC/QRC_Overview.htm

Q-SYS Remote Control (QRC) is the newer and most advanced means to allow an external control system to control various functions within Q-SYS. As opposed to ECP, which requires the use of Named Controls, QRC allows multiple levels of control at the component level. And, unlike ECP, you do not need to drag every control you want to control into the Named Controls pane.

## Features

- **Named Controls** - Control named controls
- **Control Script** - Control any control within any component by customizing the name of the component to make it unique
- **Mixer Control** - Specialized control of mixers using mixer concepts
- **PA Router Control** - A powerful API for integrating third-party control of the PA Router functionality

## Connection
- Port: **1710**
- Protocol: JSON RPC 2.0, null-terminated commands

## Sections
- Requirements
- Connections
- Change Groups
- Controlling Redundant Cores
- QRC Commands
- PARAPI (PA Router API)
