# QIO-S4

> 来源: https://help.qsys.com/q-sys_10.4/#Hardware/IO_Expanders/QIO-S4.htm
> 抓取时间: 2026-10-13

## 概述 / Overview

Q-SYS QIO-S4 是 Q-SYS 生态原生的网络控制端点，作为 IP-to-serial 桥接器，实现基于网络的控制分发。紧凑型设计支持表面安装，可选机架套件将 1-4 台设备装入标准 1U 十九英寸机架。最多 4 台设备可通过一个接入交换机端口级联（需 +24 VDC 供电），也可每台单独通过以太网供电（PoE）。

## 特性 / Features

- Q-SYS 原生控制 I/O 扩展器
- 4 个串行端口（COM1 可配置，COM2-4 专用于 RS232）
- PoE 供电
- 支持 Q-SYS Designer 拖放集成和 Q-SYS Reflect 管理
- 表面或机架安装

## 设计组件 / Design Components

库存组件：
- Status (NL Series, NM Series, QIO Series)
- Serial Port (QIO-S4) — COM1 可在属性中配置为 RS232 / RS485 Half Duplex TX / RS485 Half Duplex RX / RS485-422 Full Duplex

## 串行端口引脚定义 / Serial Port Pinouts

### COM 1（可配置）/ COM 2-4（专用 RS232）— RS232

| 引脚 | 信号方向 | 说明 |
|------|----------|------|
| (GND) | N/A | Signal ground |
| TX | Output | Transmit data |
| RX | Input | Receive data |
| RTS | Output | Ready to Send（硬件流控时） |
| CTS | Input | Clear to Send（硬件流控时） |

### RS485 Half Duplex TX 或 RX — COM 1（可配置）

| 引脚 | 信号方向 | 说明 |
|------|----------|------|
| (GND) | N/A | Signal ground |
| **TX** | Input/Output | **Differential B-** |
| RX | (Unused) | (Unused) |
| **RTS** | Input/Output | **Differential A+** |
| CTS | (Unused) | (Unused) |

> **关键**: RS485 半双工模式下，A+ 接 RTS 引脚，B- 接 TX 引脚。RX 和 CTS 不使用。

### RS485/422 Full Duplex — COM 1（可配置）

| 引脚 | 信号方向 | 说明 |
|------|----------|------|
| (GND) | N/A | Signal ground |
| TX | Output | Differential Z- / Tx- |
| RX | Input | Differential A+ / Rx+ |
| RTS | Output | Differential Y+ / Tx+ |
| CTS | Input | Differential B- / Rx- |

## 设备复位 / Device Reset

- **Short Reset**（按住约10秒，LED慢闪）：恢复 IP 为 Auto(DHCP)，删除静态路由，保留主机名
- **Long Reset**（按住约20秒，LED快闪，30秒内再按确认）：恢复出厂设置，清除所有网络设置、证书、日志、密码
