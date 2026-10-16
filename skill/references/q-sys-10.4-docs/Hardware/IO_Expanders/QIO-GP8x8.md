# QIO-GP8x8

> 来源: https://help.qsys.com/q-sys_10.4/#Hardware/IO_Expanders/QIO-GP8x8.htm
> 抓取时间: 2026-10-13

## 概述 / Overview

Q-SYS QIO-GP8x8 是 Q-SYS 生态原生的网络控制端点，提供通用输入/输出（GPIO）连接，使 Q-SYS 网络能够与外部设备（如 LED 指示器、开关、继电器、电位器）以及自定义或第三方控制接口对接。

## 特性 / Features

- Q-SYS 原生控制 I/O 扩展器
- 8 路逻辑输入 + 8 路逻辑输出
- PoE 供电（Type 1 Class 3）
- 最多 4 台级联（需本地直流供电）
- Q-SYS Designer 拖放集成，Q-SYS Reflect 管理
- 表面或机架安装（QIO-RMK 另购）

## 设计组件 / Design Components

- Status (NL Series, NM Series, QIO Series)
- GPIO In (QIO Devices) — 8 路输入
- GPIO Out (QIO Series) — 8 路输出

## 接口定义 / Connections and Callouts

### 前面板
- Power LED — 上电时亮蓝色
- ID LED — ID 模式时闪绿色
- ID Button — 在 Designer 中定位设备

### 后面板
- External Power Input — 24V DC 2.5A，2-pin Euro 连接器
- Daisy-Chain Power Output — 24V DC 2.5A，级联供电输出
- LAN [PoE] — RJ-45，PoE Type 1 Class 3，Q-LAN
- LAN [THRU] — RJ-45，以太网级联
- Device Reset — 恢复默认网络设置
- **12V DC .1A Out** — GPIO 用，黑色连接器引脚 1 和 11
- **GPIO Inputs** — 8 路输入，0-24V 模拟输入/数字输入/触点闭合，可配置上拉至 +12V（引脚 1-8）
- **Signal Ground** — GPIO 用地，黑色连接器引脚 10 和 20
- **GPIO Outputs** — 8 路输出，开集电极（24V，0.2A sink 最大），上拉至 +3.3V（引脚 1-8）

## 设备复位 / Device Reset

- Short Reset（约10秒，LED慢闪）：恢复 IP 为 Auto(DHCP)，删除静态路由，保留主机名
- Long Reset（约20秒，LED快闪，30秒内确认）：恢复出厂设置
