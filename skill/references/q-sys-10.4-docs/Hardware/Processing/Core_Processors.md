# Q-SYS Core 处理器（Processing）

> 来源: https://help.qsys.com/q-sys_10.4/#Hardware/Processing/
> 抓取时间: 2026-10-13
> 用途: qplug 开发平台参考

## Core 型号对比 / Core Model Comparison

| 型号 | 网络I/O | 板载I/O | Dante | USB音频 | AEC | VoIP | GPIO | RS232 | 外设上限 | 尺寸 |
|------|---------|---------|-------|---------|-----|------|------|-------|----------|------|
| Core Nano | 64x64 | N/A | 8x8(最高32x32) | 8x8 | 8 | 2 | N/A | 2 | 32 | 1/2机架 1RU |
| Core 8 Flex | 64x64 | 8 flex | 8x8(最高32x32) | 8x8 | 8 | 2 | 8x8 | 2 | 32 | 1/2机架 1RU |
| Core 110f | 128x128 | 8 in/8 out | 8x8(最高128x128) | 16x16 | 16 | 16 | 8x8 | 2 | 64 | 1RU |
| Core 24f | 128x128 | 24 flex | 8x8(最高128x128) | 16x16 | 16 | 16 | 8x8 | 2 | 64 | 1RU |
| Core 510i | 256x256 | 可插卡 | 8x8(最高256x256) | 16x16 | 64 | 64 | 可插卡 | 2 | 128 | 2RU |
| Core 610 | 256x256 | N/A | 8x8(最高256x256) | N/A | 64 | 64 | N/A | 1 | 128 | 1RU |
| Core 110c | 128x128 | 24(8in/8out/8flex) | — | 16x16 | 4 | 4 | — | — | 32 | 1RU(影院) |
| Core 510c | 256x256 | 可插卡 | — | 16x16 | 64 | 64 | 可插卡 | 2 | 128 | 2RU(影院) |
| Core 5200 | 512x512 | 可插卡 | 8x8(最高512x512) | 16x16 | 128 | 128 | 可插卡 | 2 | 256 | 3RU |
| Core 6000 CXR | 512x512 | 可插卡 | 8x8(最高512x512) | 16x16 | 128 | 128 | 可插卡 | 2 | 256 | 3RU(冗余) |
| Server Core X10 | 256x256 | N/A | 8x8(最高256x256) | N/A | 64 | 64 | N/A | N/A | 128 | 1RU(服务器) |
| Server Core X20r | 512x512 | N/A | 8x8(最高512x512) | N/A | 128 | 128 | N/A | N/A | 256 | 2RU(冗余服务器) |
| Server Core X50r | 1024x1024 | N/A | 8x8(最高1024x1024) | N/A | 256 | 256 | N/A | N/A | 512 | 2RU(冗余服务器) |
| NV-32-H (Core Capable) | 64x64 | 32 HDMI | 8x8 | 16x16 | 16 | 16 | N/A | N/A | 32 | 1RU(视频端点) |

## 设计组件 / Design Components

所有 Core 模式下通用组件：
- **Status (Core)** — 处理器状态监控
- **Serial Port (Core and I/O Devices)** — RS232 串口控制
- **Loudspeaker Monitor** — 扬声器监控

## 模式切换 / Mode Switching

Core Nano 和 Core 8 Flex 支持 Core Mode / Peripheral Mode 切换：
- **Core Mode**: 独立音频和控制处理单元
- **Peripheral Mode**: 作为 I/O 外设连接到主 Core

切换方法：Core Manager > Utilities > Mode > Switch

## Q-SYS 外设上限说明 / Peripheral Limit

包含原生 Q-SYS 摄像头、I/O（含 NL）、NV、TSC、寻呼站、扩展和 "Is Managed"=Yes 的插件。不包含 Streaming I/O、扬声器、脚本和 "Is Managed"=No 的插件。

## 关键接口 / Key Interfaces

### 前面板
- Status/ID 指示灯
- LCD 显示屏（显示 Core 名称、状态、健康警报）
- 电源按钮
- USB 端口（部分型号不支持）
- ID 按钮

### 后面板
- Q-SYS LAN 端口（RJ45，1000Mbps）：LAN A, LAN B, AUX A, AUX B
- RS232 串口（DE-9 公头）
- 电源单元
- 板载 I/O（型号不同而异）
- GPIO 端口（部分型号）
