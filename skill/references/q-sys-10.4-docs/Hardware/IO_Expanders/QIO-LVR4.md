# QIO-LVR4

> 来源: https://help.qsys.com/q-sys_10.4/#Hardware/IO_Expanders/QIO-LVR4.htm
> 抓取时间: 2026-10-13

## 概述 / Overview

Q-SYS QIO-LVR4 扩展 Q-SYS 系统能力，通过低压继电器连接实现与非网络化控制设备的简化互操作。通过将本地 I/O 与处理硬件分离，QIO 系列提供模块化、可扩展的网络 I/O，支持所需的拓扑结构。

## 特性 / Features

- Q-SYS 原生低压继电器扩展器
- 4 路低压继电器输出
- PoE 供电
- 最多 4 台级联（需本地直流供电）
- Q-SYS Designer 拖放集成

## 设计组件 / Design Components

- Status (NL Series, NM Series, QIO Series)
- Relay Out (QIO Series) — 4 路继电器输出

## 接口定义 / Connections and Callouts

### 前面板
- Power LED / ID LED / ID Button
- 继电器状态指示灯

### 后面板
- External Power Input — 24V DC 2.5A
- Daisy-Chain Power Output — 24V DC 2.5A
- LAN [PoE] — RJ-45，PoE
- LAN [THRU] — 以太网级联
- Device Reset
- Relay Outputs — 4 路低压继电器，端子块连接

## 设备复位 / Device Reset

- Short Reset（约10秒）：恢复网络设置
- Long Reset（约20秒+确认）：恢复出厂设置
