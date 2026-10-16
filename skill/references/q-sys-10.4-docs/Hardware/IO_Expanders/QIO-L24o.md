# QIO-L24o

> 来源: https://help.qsys.com/q-sys_10.4/#Hardware/IO_Expanders/QIO-L24o.htm
> 抓取时间: 2026-10-13

## 概述 / Overview

Q-SYS QIO-L24o 是 Q-SYS 生态原生的网络音频端点，提供 24 路线性输出，实现基于网络的音频分发。1RU 机架空间内高密度集成 24 个模拟音频连接。配备 8x8 GPIO 控制端口，双以太网支持网络冗余，两台设备可组成冗余故障切换对。

## 特性 / Features

- 24 路线性电平输出
- 支持网络和外设冗余
- 1RU 机架
- 8x8 GPIO 第三方设备控制
- 输出集成继电器静音，支持冗余音频输出，防止上电瞬态
- 双千兆以太网端口
- QIO-CK 冗余电缆套件（另购）

## 设计组件 / Design Components

- Status (NL Series, NM Series, QIO Series)
- Line Out (QIO Series) — 24 路
- GPIO In (QIO Devices) — 8 路
- GPIO Out (QIO Series) — 8 路

## 接口定义 / Connections

### 后面板右侧
- LAN 端口（双）— 最高 1 Gbps
- AC 电源输入 — 通用国际电源
- GPIO 输入（8 引脚，2-9）— 0-24VDC 模拟/电位器/TTL 数字/触点闭合
- GPIO 输出（8 引脚，2-9）— 开集电极（24V，0.2A 最大），上拉至 3.3V 或 TTL 输出
- 接地参考（每个连接器引脚 10）
- 12VDC 电源（每个连接器引脚 1），每引脚最高 0.2A

### 后面板左侧
- Line Outputs（24 通道，绿色）— 平衡或非平衡
