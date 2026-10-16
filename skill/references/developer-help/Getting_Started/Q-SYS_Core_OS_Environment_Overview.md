# Q-SYS Core OS Environment Overview

> 来源: https://help.qsys.com/DeveloperHelp/#Getting_Started/Q-SYS_Core_OS_Environment_Overview.htm

## Applications

The Q-SYS Core OS Platform is a Linux-based application that runs on a Q-SYS Core processor. Two major sub-applications:

- **Audio engine**: Manages DSP processing, processes 3000 audio frames per second (fps)
- **Runtime engine**: Handles all control changes and syncing between Core OS Platform and Core processor. All Lua scripting runs on the Runtime engine.

Q-SYS Designer Software (QDS) is a Windows application, front-end DSP and programming tool. Can emulate the Runtime engine locally.

## Key Timing

- Runtime engine processes control changes at **30 fps**
- Control values transferred to DSP coefficients every **33 ms**
- Setting a control value faster than 30 times/second has no effect

## Threading

All Lua scripts (plugins, Block Controller, etc.) run on a **single thread**, sharing resources. If one script hits max executions, it prevents other scripts from running.

## Lua in Q-SYS

- Uses **Lua 5.3** with most standard libraries
- Q-SYS specific extensions added for common install functionality
- Plugins: single .qplug file placed in QSC directory within 'My Documents'

## Design Time vs Runtime

- **Design Time (pre-compile)**: Graphics and properties processed by Q-SYS Designer's Design Time engine. Changes require redeploy to Core.
- **Runtime**: Control values managed by Runtime engine, like any other Lua script.
