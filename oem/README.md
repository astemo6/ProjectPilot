# OEM-Gantt

**中文** · [English](#english) · [Deutsch](#deutsch)

- 在线地址 / Online: https://astemo6.github.io/ProjectPilot/oem/
- ProjectPilot（完整排程 / full scheduling / vollständige Planung）: https://astemo6.github.io/ProjectPilot/

## 中文

客户节点计划工具：选择主机厂、填写客户节点日期，自动生成给主机厂的节点甘特图。

- 16 家主机厂的客户节点模板及节点说明
- 阶段色带（APQP 等）、推荐任务、供应商节点、自定义任务
- 日期倒置标红；节点密集时标签自动错开
- 预览，导出 PDF / JPG（可加 Logo、制作者、日期）
- 项目文件导出 / 导入（JSON）
- 中文 / English / Deutsch；浅色 / 深色 / 跟随系统；中国节假日与调休

### 最近更新

- 2026-10-15：甘特图上可左右拖动菱形（客户节点、供应商节点）直接改日期；导出前弹出确认框，可选择保存位置
- 2026-10-15：供应商节点填入日期后自动按日期排到合适位置；新增自定义任务也按开始日期插入
- 2026-10-15：BMW 默认不勾选节点 2、3、7、8、9、11、12；「推荐任务（模板）」默认折叠（切换任何 OEM 都重新折叠）
- 2026-10-14：顶栏新增 ↶撤销 / ↷重做（Ctrl+Z / Ctrl+Y）；去掉未选客户时的下拉框高亮
- 2026-10-14：去掉顶部「第一步：选择客户」提示条
- 2026-10-14：甘特图左列宽、里程碑行高可在图上拖动，或在图例右侧填数值调整（「自动」恢复自适应），导出 PDF/JPG 同步生效
- 2026-10-14：修复导出的 PDF 在 Adobe Acrobat 中打不开；日期框右侧可点日历选择日期；导出文件名始终使用当前完整项目名（不再截断，/ 等字符改为 -）
- 2026-10-13：README 增加英文、德文说明
- 2026-10-12：与 ProjectPilot 统一：顶栏最右为主题和语言切换；新增暗色界面（导出仍为白底）
- 2026-10-12：地址改为 /oem/；右侧入口「ProjectPilot ↗」
- 2026-10-12：macOS 风格界面；顶栏合并为一行；修复里程碑标签重叠、Esc 关预览；导出文件名统一

## English

Customer milestone planner: pick an OEM, enter its milestone dates, and get a milestone Gantt chart ready to send to the customer.

- Milestone templates and descriptions for 16 OEMs
- Phase bands (APQP etc.), suggested tasks, supplier milestones, custom tasks
- Out-of-order dates highlighted in red; labels staggered automatically when dense
- Preview and export to PDF / JPG (optional logo, author, date)
- Project file export / import (JSON)
- Chinese / English / German; light / dark / system theme; Chinese holidays and make-up workdays

## Deutsch

Planer für Kundenmeilensteine: OEM wählen, Meilensteintermine eintragen und ein Meilenstein-Gantt-Diagramm für den Kunden erzeugen.

- Meilensteinvorlagen und Beschreibungen für 16 OEMs
- Phasenbänder (APQP usw.), empfohlene Vorgänge, Lieferantenmeilensteine, eigene Vorgänge
- Termine in falscher Reihenfolge werden rot markiert; Beschriftungen werden bei Dichte automatisch versetzt
- Vorschau und Export als PDF / JPG (optional Logo, Ersteller, Datum)
- Export / Import von Projektdateien (JSON)
- Chinesisch / Englisch / Deutsch; helles / dunkles / System-Design; chinesische Feiertage und Ersatzarbeitstage

Data is stored only in your browser. / Daten werden nur im Browser gespeichert. / 数据只保存在本机浏览器。
