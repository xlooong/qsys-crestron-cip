# WebSocket

> 来源: https://help.qsys.com/q-sys_10.4/#Control_Scripting/WebSocket.htm
> 入库时间: 2026-10-16
> 用途: Q-SYS Lua WebSocket 扩展

## 概述 / Overview

WebSocket 提供两种通信机制，用于运行在受控环境（Core）中的客户端代码与已订阅该代码通信的远程主机之间的双向通信：

- **发送消息**（sending messages）
- **接收消息**（receiving messages）

## 安全模型 / Security Model

安全模型基于**客户端请求的来源（origin）**。WebSocket 通过验证客户端的 origin 来建立信任关系。

## 两种通信机制 / Two Mechanisms

WebSocket 允许两种通信机制：

1. **发送消息** — 客户端代码向远程主机发送数据
2. **接收消息** — 客户端代码接收远程主机发来的数据

## 要点 / Key Points

- 基于 origin 的安全模型，远程主机可校验客户端来源
- 支持双向实时通信，适合控制类应用
- 与 TCP Socket 不同，WebSocket 是浏览器/Web 标准协议，带握手和帧封装
