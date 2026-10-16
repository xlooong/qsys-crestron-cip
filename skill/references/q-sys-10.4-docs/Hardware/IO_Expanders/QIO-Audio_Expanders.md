# QIO-ML4i / QIO-L4o / QIO-ML2x2 / QIO-AES8x8 / QIO-TEL2

> 来源: https://help.qsys.com/q-sys_10.4/#Hardware/IO_Expanders/QIO-ML4i.htm
> 抓取时间: 2026-10-13

## 概述 / Overview

QIO 系列网络音频 I/O 扩展器，紧凑型设计，支持表面安装或机架安装（1U 最多 4 台）。最多 4 台级联（需 24VDC 供电），也可单独 PoE 供电。

## 型号对比 / Model Comparison

| 型号 | 音频输入 | 音频输出 | 其他 |
|------|----------|----------|------|
| QIO-ML4i | 4 路 Mic/Line | — | +48V 幻象电源，麦克风检测 |
| QIO-L4o | — | 4 路 Line | — |
| QIO-ML2x2 | 2 路 Mic/Line | 2 路 Line | +48V 幻象电源 |
| QIO-AES8x8 | 4 路 AES3 输入 | 4 路 AES3 输出 | 数字音频 |
| QIO-TEL2 | 2 路 PSTN (POTS) | — | 电话接口 |

## 共同特性 / Common Features

- Q-SYS 原生音频 I/O 扩展器
- 专业 Mic/Line 电平输入，+48V 幻象电源
- 输入麦克风检测（监控、使用统计、故障通知）
- PoE 供电（Type 1 Class 2/3）
- 最多 4 台级联
- Q-SYS Designer 拖放集成，Q-SYS Reflect 管理
- 表面或机架安装（QIO-RMK 另购，QIO-PSU 另购）

## 设计组件 / Design Components

### QIO-ML4i
- Status (NL Series, NM Series, QIO Series)
- Mic/Line In (QIO Series) — 4 路

### QIO-L4o
- Status (NL Series, NM Series, QIO Series)
- Line Out (QIO Series) — 4 路

### QIO-ML2x2
- Status (NL Series, NM Series, QIO Series)
- Mic/Line In (QIO Series) — 2 路
- Line Out (QIO Series) — 2 路

### QIO-AES8x8
- Status (NL Series, NM Series, QIO Series)
- AES3 In (QIO Series) — 4 路
- AES3 Out (QIO Series) — 4 路

### QIO-TEL2
- Status (NL Series, NM Series, QIO Series)
- Telco (QIO Series) — 2 路 POTS

## 接口定义 / Connections

### 前面板
- Power LED — 上电亮蓝色
- ID LED — ID 模式闪绿色
- ID Button — Designer 中定位设备

### 后面板
- External Power Input — 24V DC 2.5A，2-pin Euro
- Daisy-Chain Power Output — 24V DC 2.5A
- LAN [PoE] — RJ-45，PoE，Q-LAN
- LAN [THRU] — RJ-45，以太网级联
- Device Reset — 恢复默认网络设置
- 音频接口（型号不同而异）
