# QIO-IR1x4

> 来源: https://help.qsys.com/q-sys_10.4/#Hardware/IO_Expanders/QIO-IR1x4.htm
> 抓取时间: 2026-10-13

## 概述 / Overview

Q-SYS QIO-IR1x4 是 Q-SYS 生态原生的网络控制端点，作为 IP-to-IR 桥接器，实现基于网络的红外控制分发。

## 特性 / Features

- Q-SYS 原生 IP-to-IR 桥接器
- 1 路红外输入 + 4 路红外输出
- PoE 供电
- 最多 4 台级联（需本地直流供电）
- Q-SYS Designer 拖放集成

## 设计组件 / Design Components

- Status (NL Series, NM Series, QIO Series)
- IR Output (QIO Devices) — 4 路红外输出
- IR Input (QIO Devices) — 1 路红外输入（学习/接收）

## 接口定义 / Connections and Callouts

### 前面板
- Power LED — 上电亮蓝色
- ID LED / ID Button

### 后面板
- External Power Input — 24V DC 2.5A
- Daisy-Chain Power Output — 24V DC 2.5A
- LAN [PoE] — RJ-45，PoE
- LAN [THRU] — 以太网级联
- Device Reset
- IR Input — 3.5mm 接口，用于红外学习/接收
- IR Outputs 1-4 — 3.5mm 接口，连接红外发射棒

## IR 端口引脚定义 / IR Port Pinouts

IR Output（3.5mm TRS）:
- Tip — IR Signal
- Ring — +12V DC（为红外发射棒供电）
- Sleeve — GND

IR Input（3.5mm TRS）:
- Tip — IR Signal
- Ring — N/C
- Sleeve — GND

## 设备复位 / Device Reset

- Short Reset（约10秒）：恢复网络设置
- Long Reset（约20秒+确认）：恢复出厂设置
