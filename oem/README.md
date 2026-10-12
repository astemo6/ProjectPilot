# OEM-Gantt

客户节点计划工具：选择主机厂、填写客户节点日期，自动生成给主机厂的节点甘特图。

- 在线地址：https://astemo6.github.io/ProjectPilot/oem/
- 完整排程工具：顶栏「ProjectPilot ↗」，或 https://astemo6.github.io/ProjectPilot/

## 主要功能

- 16 家主机厂的客户节点模板及节点说明
- 阶段色带（APQP 等）、推荐任务、供应商节点、自定义任务
- 日期倒置标红；节点密集时标签自动错开
- 预览，导出 PDF / JPG（可加 Logo、制作者、日期）
- 项目文件导出 / 导入（JSON）
- 中文 / English / Deutsch；浅色 / 深色 / 跟随系统；中国节假日与调休

## 最近更新

- 2026-10-12：与 ProjectPilot 统一：顶栏最右为主题（浅色 / 暗色 / 跟随系统，两边共用设置）和语言切换；新增暗色界面（导出仍为白底）
- 2026-10-12：地址改为 /oem/；右侧入口「ProjectPilot ↗」
- 2026-10-12：macOS 风格界面；顶栏合并为一行；修复里程碑标签重叠、Esc 关预览；导出文件名统一

## 文件

- `index.html` 外壳与顶栏，`plan.html` 客户节点页，`workcal.js` 工作日历
- 数据保存在本机浏览器（`gantt-tool-v1`）
