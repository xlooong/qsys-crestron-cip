# QIO-FLEX4A

> 来源: https://help.qsys.com/q-sys_10.4/#Hardware/IO_Expanders/QIO-FLEX4A.htm
> 抓取时间: 2026-10-13

## 概述 / Overview

QIO-FLEX4A 是一体化网络 I/O 外设，专为演示、讨论和互联协作空间设计。

## 特性 / Features

- 一体化网络 I/O 外设
- 适用于演示、讨论、协作空间
- PoE 供电
- Q-SYS Designer 拖放集成

## 设计组件 / Design Components

- Status (NL Series, NM Series, QIO Series)
- 具体音频/控制组件以 Designer 库存为准

## 接口定义 / Connections and Callouts

### 前面板
- Power LED / ID LED / ID Button

### 后面板
- LAN [PoE] — RJ-45，PoE
- 音频输入/输出接口（具体以产品规格为准）
- GPIO 接口
- Device Reset

## 设备复位 / Device Reset

- Short Reset（约10秒）：恢复网络设置
- Long Reset（约20秒+确认）：恢复出厂设置

> 注：详细规格和安装文档请参考 QSC 官网 FLEX4A 产品页面。
