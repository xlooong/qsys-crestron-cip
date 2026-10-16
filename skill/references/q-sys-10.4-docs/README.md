# Q-SYS 10.4 Documentation Knowledge Base

> 来源: https://help.qsys.com/q-sys_10.4/
> 抓取时间: 2026-10-12（Schematic_Library/Designer/Hardware 补抓: 2026-10-16）
> 用途: qplug 开发参考知识库
> 已抓取: 190+ 个页面（含 Hardware、Designer、CSS/UCI）

## 目录结构 / Directory

### Control_Scripting/ - 控制脚本（Lua 开发）✅ 36/39 扩展已抓取

| 文件 | 说明 |
|------|------|
| 01_Using_Lua_in_Q-Sys_Overview.md | Control Scripting 总览 |
| Q-SYS_Extensions_to_Lua.md | Q-SYS Lua 扩展索引（35个API） |
| TcpSocket.md | TCP 客户端套接字 |
| TcpSocketServer.md | TCP 服务端套接字 |
| Timer.md | 定时器 |
| Controls_IO.md | 控件输入输出 |
| Component.md | 命名组件访问 |
| NamedControl.md | 命名控件读写 |
| SerialPorts.md | RS-232 串口通信 |
| SerialServerPorts.md | 虚拟串口服务 |
| UDPSocket.md | UDP 套接字 |
| HttpClient.md | HTTP/HTTPS 客户端 |
| JSON.md | JSON 编解码（旧版） |
| RapidJSON.md | 快速 JSON（推荐） |
| System.md | 系统环境信息 |
| Design.md | 设计状态与清单 |
| Network.md | 网络接口与DNS |
| Snapshot.md | 快照管理 |
| Mixer.md | 混音器控制 |
| ChannelGroup.md | 通道组索引 |
| Crypto.md | 加密/Base64/MD5/HMAC |
| Log.md | 系统日志写入 |
| Uci.md | UCI 编程控制 |
| Email.md | 邮件发送 |
| Ping.md | ICMP Ping |
| Notifications.md | 脚本间通知 |
| QRCode.md | QR 码生成 |
| Ssh.md | SSH 客户端 |
| SNMP.md | SNMP 管理 |
| SNMPTrap.md | SNMP Trap 接收 |
| LuaDate.md | 日期时间处理 |
| LuaXML.md | XML 解析 |
| LPeg.md | PEG 模式匹配 |
| Lua_bitstring.md | 位串操作 |
| EzSVG.md | 动态 SVG 生成 |
| WebSocket.md | WebSocket 双向通信（origin 安全模型） |
| Dante_API.md | Dante API（DanteBrowser 设备发现 + DanteDevice GPIO 控制） |
| Lua_USB_HID.md | USB HID 输入（UsbMonitor 设备插拔 + Uab 按键/轴/按钮事件） |
| dir.md | 目录操作（dir.get/create/remove，仅限 media/ 和 design/） |

> 原标记 404 的 WebSocket、Dante API、Lua USB HID、dir 已由用户提供 PDF 于 2026-10-16 全部入库 ✅

### External_Control/ - 外部控制 API ✅ 已完成

| 文件 | 说明 |
|------|------|
| External_Control_APIs_Overview.md | 六大API总览（QRC/ECP/QRWC/NPM/Communications/Change Groups） |
| QRC_Overview.md | QRC协议总览（端口1710，JSON RPC 2.0） |
| QRC_Commands.md | QRC完整命令参考（23606字符，含所有方法与错误码） |
| ECP_Overview.md | ECP协议总览（legacy端口1702） |
| Change_Groups.md | Change Groups详解（最多512个，Lua脚本消耗1个slot） |

### Schematic_Library/ - 组件库 ✅ 62 个页面已完成（57 个组件 + 5 个概述/自定义页，2026-10-16 补齐）

#### Scripting Components（脚本组件）
| 文件 | 说明 |
|------|------|
| Control_Script.md | Control Script（Lua脚本，Input/Output Count，Start Automatically） |
| Text_Controller.md | Text Controller（自定义控件+Lua文本编辑器，支持Panels） |
| Block_Controller.md | Block Controller（可视化块编程，支持Connections） |

#### Control Components（控制组件）
| 文件 | 说明 |
|------|------|
| Command_Buttons.md | Command Buttons（最多64按钮，TCP/UDP/Serial发码） |
| Custom_Controls.md | Custom Controls（最多10组×32控件，自定义控制引脚） |
| Control_Function.md | Control Function（逻辑运算） |
| Control_Router.md | Control Router（控制信号路由，Crosspoint/Knob/Combo） |
| Control_Delay.md | Control Delay（0ms-60s延迟，1-32输出） |
| When.md | When（按星期+时间调度事件） |
| Selector.md | Selector（多值选择器，互斥按钮） |
| Sequencer.md | Sequencer（序列器） |
| Status_Combiner.md | Status Combiner（状态合并，1-512输入） |
| Flip_Flop.md | Flip-Flop（trigger转Boolean，Set/Reset/Toggle） |
| Value_Stepper.md | Value Stepper（值步进器，integer/gain/percentage） |
| Press_and_Hold.md | Press and Hold（长按/短按区分触发） |
| Date_Time.md | Date/Time（日期时间文本，Custom格式） |
| Event_Log.md | Event Log（显示最后一条事件日志） |
| Event_Logger.md | Event Logger（写入事件日志，支持参数） |
| Blinking_LED.md | Blinking LED（闪烁LED，可作方波输入） |
| Astronomical_Clock.md | Astronomical Clock（日出/日落/正午触发，需联网） |
| Color_Picker.md | Color Picker（颜色选择器，输出hex码） |
| Contact_List.md | Contact List（通讯录，拨号集成） |
| Control_Link.md | Control Link（跨设计控制链接，Server/Client模式） |
| Emailer.md | E-mailer（邮件发送，最大16KB） |
| Envelope_Generator.md | Envelope Generator（包络发生器，Attack/Sustain/Release） |
| GPS_Info.md | GPS Info（GPS接收器信息，NMEA 0183） |
| IR_Driver.md | IR Driver（红外命令发送，品牌/型号数据库） |
| IR_Receiver.md | IR Receiver（红外学习与保存） |
| LFO.md | LFO（低频振荡器，控制信号输出） |
| PIN_Pad.md | PIN Pad（PIN码验证，UCI页面访问控制） |
| Call_Sync.md | Call Sync（通话同步，USB HID/Softphone/POTS） |
| Ping.md | Ping（网络可达性检测） |
| SNMP_Query.md | SNMP Query（最多16 OID监控） |
| UCI_Layer_Controller.md | UCI Layer Controller（UCI图层显示/隐藏） |
| UCI_Style_Controller.md | UCI Style Controller（UCI样式动态切换） |
| USB_Router.md | USB Router（USB HID信号路由） |

#### Monitor Components（监控组件）
| 文件 | 说明 |
|------|------|
| Signal_Presence.md | Signal Presence（音频信号存在检测） |

#### Audio Components（音频组件）
| 文件 | 说明 |
|------|------|
| Gain.md | Gain（增益，最多256通道） |
| Gain_Ramp.md | Gain Ramp（增益渐变，双向ramp） |
| Delay.md | Delay（延迟，最多256通道×512 Taps，3种类型） |
| Crossover.md | Crossover（分频器，2-6频段，4种滤波器） |
| Crossfader.md | Crossfader（交叉淡入淡出） |
| Room_Combiner.md | Room Combiner（房间合并，最多8房间） |
| Router.md | Router（音频路由，Crosspoint/Knob/Combo） |
| System_Mute.md | System Mute（系统静音，panic按钮） |
| Audio_File_Recorder.md | Audio File Recorder（音频录制，1-4轨） |
| Acoustic_Echo_Canceler.md | Acoustic Echo Canceler（回声消除） |
| Voice_Activity_Detector.md | Voice Activity Detector（语音活动检测） |
| Timeline.md | Timeline (BETA)（时间线音频播放） |

#### Video Components（视频组件）
| 文件 | 说明 |
|------|------|
| AV_Stream_Router.md | AV Stream Router（AV流路由，NV-32-H） |
| Camera_Router.md | Camera Router（摄像头路由，Mediacast） |
| Mediacast_Router.md | Mediacast Router（Mediacast视频路由） |
| NVM_Proxy.md | NVM Proxy（NVM设备虚拟控制管理） |
| VisionSuite.md | VisionSuite（房间感知控制，3D可视化） |

#### Layout Components（布局组件）
| 文件 | 说明 |
|------|------|
| Channel_Group.md | Channel Group (BETA)（DSP组件组自动复制） |
| Container.md | Container（组件分组折叠，最多100入/100出，支持密码） |
| Popup_Button.md | Popup Button（弹出窗口，减少原理图 clutter） |
| Signal_Snakes.md | Signal Snakes（信号束，1-256通道混合类型） |

#### Other（其他）
| 文件 | 说明 |
|------|------|
| Inventory.md | Inventory（硬件清单管理） |
| UCI_Design_Overview.md | UCI Design Overview（UCI设计总览） |
| UCI_Customization.md | UCI Customization（UCI自定义，Pages/Layers/Navigation） |
| Snapshots.md | Snapshots（快照，Global + Snapshot Banks） |

### Hardware/ - 硬件文档 ✅ 45+ 页面已抓取

#### Processing（Core 处理器）
| 文件 | 说明 |
|------|------|
| Core_Processors.md | 14 款 Core 处理器对比（Nano/8Flex/110f/24f/510i/610/110c/510c/5200/6000CXR/X10/X20r/X50r/NV-32-H），含网络I/O、板载I/O、Dante、AEC、VoIP、GPIO、RS232、外设上限、模式切换 |

#### IO_Expanders（I/O 扩展器）
| 文件 | 说明 |
|------|------|
| QIO-S4.md | 4路串口扩展器，RS232/RS485半双工/RS485-422全双工引脚定义（**RS485半双工: RTS=A+, TX=B-**） |
| QIO-GP8x8.md | 8路GPIO输入输出，0-24V输入，开集电极输出 |
| QIO-IR1x4.md | 1路IR输入+4路IR输出，3.5mm引脚定义 |
| QIO-FLEX4A.md | 一体化协作空间I/O |
| QIO-LVR4.md | 4路低压继电器 |
| QIO-L24o.md | 24路线性输出+8x8 GPIO |
| QIO-Audio_Expanders.md | ML4i/L4o/ML2x2/AES8x8/TEL2 型号对比 |
| QIO-24f.md | 高密度24通道flex I/O（8 mic/line输入+8 FLEX+8 line输出+8x8 GPIO） |
| QIO-ML24i.md | 高密度24通道麦克风输入 |

#### Control_IO（触摸屏控制器）
| 文件 | 说明 |
|------|------|
| TSC-101-G3.md | 10.1" G3 触摸屏 |
| TSC-116w-G2.md | 11.6" G2 宽屏触摸屏 |
| TSC-47w-G2.md | 4.7" G2 宽屏触摸屏 |
| TSC-50-G3.md | 5" G3 触摸屏 |
| TSC-55w-G2.md | 5.5" G2 宽屏触摸屏 |
| TSC-70-G3.md | 7" G3 触摸屏 |
| TSC-80w-G2.md | 8" G2 宽屏触摸屏 |
| TSC_Inventory_Status.md | TSC 库存/状态说明 |

#### Video（视频设备）
| 文件 | 说明 |
|------|------|
| NC-110.md | 4K 会议摄像机 |
| NC-90-G2.md | 会议摄像机 G2 |
| NC-Pro15x.md | Pro 系列 15x PTZ 摄像机 |
| NC-PTZ.md | PTZ 会议摄像机 |
| NV-1-H-WE.md | HDMI 网络视频端点（编码/解码） |
| NV-21-HU.md | 多流网络视频端点 |
| NV-32-H_Core_Capable.md | NV-32-H（Core 能力），Core/Peripheral 双模式，64x32 网络I/O |
| NVM-302D.md | 3G-SDI 网络视频监视器 |
| NVM-302E.md | 网络视频监视器 |
| VSA_100.md | 视频流适配器 |

#### Audio_Network_Amps（网络功放）
| 文件 | 说明 |
|------|------|
| CXD-Q.md | CXD-Q 系列（4/8通道） |
| CX-Q.md | CX-Q 系列（8通道） |
| MPA-Q.md | MPA-Q 系列 |
| SPA-Qf.md | SPA-Qf 系列 |

#### Page_Stations（寻呼站）
| 文件 | 说明 |
|------|------|
| Page_Station_Overview.md | 寻呼站总览 |
| PS-TSCG3_Next_Generation.md | PS-TSCG3 下一代寻呼站 |

### CSS_UCI/ - CSS 与 UCI 样式 ✅ 已完成
| 文件 | 说明 |
|------|------|
| CSS_Class_Reference.md | Q-SYS CSS 类参考（buttonprimary/buttonsecondary/icons/text类/justify类） |
| UCI_Styles.md | UCI 样式系统完整指南（31页）：创建/安装/应用样式、背景属性、图片/字体/图标字体引用、Meter/Knob/Fader 渲染样式（classic/filmstrip/layer）、动态CSS类名、按钮类型、pressed选择器、视口相对尺寸、CSS变量、@import导入 |

### Designer/ - Designer 软件使用 ✅ 19 页已完成（2026-10-16）

| 文件 | 说明 |
|------|------|
| Q-Sys_Designer_Overview.md | Designer 软件总览 |
| 0015_Installing_Q-SYS.md | 安装 Q-SYS Designer |
| 002_Getting_Started.md | 快速上手（设计文件/工作区/Emulate/Run） |
| 003_Emulate_Mode.md | Emulate 模式 |
| 013_Schematic_Library.md | 原理图组件库概览 |
| 014_Graphic_Tools.md | 图形工具 |
| 016_Check_Design.md | 设计检查 |
| Networked_Audio_Design.md | 网络音频设计 |
| properties_panel.md | 属性面板 |
| QDS_Release_Notes.md | QDS 版本说明 |
| Q-Sys_Designer_Shortcuts.md | Designer 快捷键 |
| search_and_replace.md | 查找与替换 |
| user_library.md | 用户库 |
| Using_the_Schematic.md | 原理图使用总览 |
| About_Schematic_Elements.md | 原理图元素 |
| Connections_and_Wiring_in_the_Schematic.md | 连接与布线 |
| Labeling_and_Organizing_Schematic_Elements.md | 元素标注与组织 |
| Signal_Wire_Tracing.md | 信号线追踪 |
| using_controls.md | 控件使用 |

## 使用方法 / Usage

1. 开发 qplug 时，先查阅 `references/qplug-standards.md` 了解插件框架
2. 需要某个组件的输入输出/属性/控制引脚详情时，查阅 `Schematic_Library/` 对应文件
3. 需要 Lua API 详情时，查阅 `Control_Scripting/` 对应文件
4. 需要外部控制协议时，查阅 `External_Control/` 对应文件
