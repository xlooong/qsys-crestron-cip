# wxl_personal_plug 系列规范

## 元信息

```lua
PluginInfo = {
  Name = "PluginName",
  Version = "1.0.0",
  Author = "longwang",
  Category = "wxl_personal_plug~PluginName",
  Description = "..."
}
```

- 分类统一用 `wxl_personal_plug~插件名`
- 作者统一 `longwang`
- 版本号 `主.次.修订`

## 文件位置

```
C:\Users\<user>\Documents\QSC\Q-Sys Designer\Plugins\
```

所有 qplug 直接放在 Plugins 目录下，不建子文件夹（Q-SYS 不递归扫描）。

## 命名规范

### 控件命名
- 输入：`功能_方向`，如 `Wall1Open`、`PC1_Mute`
- 输出：`功能_方向`，如 `Mic1_Mute`、`Status_Text`
- 内部状态：`_前缀`，如 `_lastValue`
- 动态数量控件：`类型_序号`，如 `Digital_In_1`、`Analog_Out_5`

### 页面命名
- 英文，首字母大写，如 `Connection`、`Monitor`、`Settings`

## 面板规范

### 必须包含
1. 顶部标题/状态区域
2. 主要控制区域（GroupBox 分组）
3. 底部 Notes 说明区域（中英文双语）

### Notes 格式
```
功能描述 / Function description
输入引脚 / Input pins:
  - Name: type, description / 类型, 说明
输出引脚 / Output pins:
  - Name: type, description / 类型, 说明
属性参数 / Properties:
  - Name: range, default, description / 范围, 默认, 说明
版本历史 / Changelog:
  - v1.0.0: initial release / 初始版本
```

### 布局规则
- 面板宽度 340px（标准），高度按需
- GroupBox 边距 8px，内部控件边距 12px
- GroupBox 高度 = 内容高度 + 30px
- 字体大小 12px（标题），11px（正文）
- 坐标仔细核对，严禁超框

## 输入按钮模式

### Toggle + 自动复位（Trigger 效果）
```lua
Controls.MyButton.EventHandler = function(c)
  if not c.Boolean then return end  -- 只响应 true
  -- 执行动作
  c.Boolean = false  -- 立即复位
end
```

### Toggle 保持状态
```lua
Controls.MyToggle.EventHandler = function(c)
  if c.Boolean then
    -- ON 逻辑
  else
    -- OFF 逻辑
  end
end
```

## 版本管理

- 每个插件独立 GitHub 仓库
- 仓库命名规范：`qsys-<kebab-case-name>`，全部小写连字符
  - 示例：`crestronCIP` → `qsys-crestron-cip`，`RoomCombineSync` → `qsys-room-combine-sync`
- GitHub 用户：`xlooong`，仓库 URL 格式：`https://github.com/xlooong/qsys-xxx`
- README 中英文双语，包含功能说明、引脚列表、使用示例
- 版本号在 PluginInfo 和 Notes 中同步更新
- 仓库可见性：核心插件公开，其余私有

## 已开发插件与 GitHub 仓库映射

| 插件名 | GitHub 仓库 | 功能 | 可见性 |
|--------|------------|------|--------|
| crestronCIP | [qsys-crestron-cip](https://github.com/xlooong/qsys-crestron-cip) | Crestron CIP 协议网关（数字/模拟/串量） | 公开 |
| RoomCombineSync | [qsys-room-combine-sync](https://github.com/xlooong/qsys-room-combine-sync) | 四房间合并麦克风同步 + 音量初始化 + 用户模式 | 私有 |
| RoomVolInit | [qsys-room-vol-init](https://github.com/xlooong/qsys-room-vol-init) | 隔墙状态变化时触发房间音量初始化 | 私有 |
| roomManual | [qsys-room-manual](https://github.com/xlooong/qsys-room-manual) | 房间模式手动切换（5预设+FlowToCater+手动覆盖） | 私有 |
| RoomUserModeSelector | [qsys-room-user-mode-selector](https://github.com/xlooong/qsys-room-user-mode-selector) | 房间用户模式选择器（Local/VC，合并模式联动） | 私有 |
| WallOpenDebounce | [qsys-wall-open-debounce](https://github.com/xlooong/qsys-wall-open-debounce) | 墙状态防抖（Retriggerable One Shot） | 私有 |
| CIPConnectFromCrestronAnalog | [qsys-cip-connect-monitor](https://github.com/xlooong/qsys-cip-connect-monitor) | 模拟量心跳检测 CIP 连接状态 | 私有 |
| System On-Off Timer | [qsys-system-on-off-timer](https://github.com/xlooong/qsys-system-on-off-timer) | 系统定时开关机（外部时间输入+周几使能） | 私有 |
| SystemCountdown | [qsys-system-countdown](https://github.com/xlooong/qsys-system-countdown) | 倒计时执行触发器 | 私有 |
| UI Material Library | [qsys-ui-material-library](https://github.com/xlooong/qsys-ui-material-library) | UI 动画素材（Spinner 等） | 私有 |
| CIPSignalTester | （未发布） | CIP 信号测试器（随机生成数字/模拟/串量） | — |
| CrestronViscaCameraTrackFb | （未发布） | Visca 摄像头追踪状态反馈 | — |
| RoomAutoSwitch | （未发布） | 信号源自动切换（队列触发） | — |
| AtlonaUsbSwitch | （未发布） | Atlona USB 切换器控制 | — |
| TriggerToMomentary | （在 qsys-crestron-cip 仓库内） | Trigger 转 Momentary（32路默认，最大500路） | — |
| Extron SW2 | （未发布） | Extron SIS 协议信号源切换 | — |
| 灯光控制 | （未发布） | 亮度/色温 DMX 码生成 + Retriggerable One Shot | — |
