# ProjectPilot

**中文** · [English](#english) · [Deutsch](#deutsch)

- 在线地址 / Online / Online: https://astemo6.github.io/ProjectPilot/
- OEM-Gantt（客户节点图 / customer milestone chart / Kundenmeilenstein-Diagramm）: https://astemo6.github.io/ProjectPilot/oem/

## 中文

项目计划排程工具（任务、资源、进度跟踪），对标 MS Project / GanttProject。单页应用，数据保存在本机浏览器。界面语言：中文 / English / Deutsch；浅色 / 深色 / 跟随系统。

### 主要功能

- **任务**：分组、里程碑、手动/自动排程、FS/SS/FF/SF 依赖与延隔、约束、期限、停用任务、周期性任务、备注与超链接
- **资源与成本**：资源工作表、分配、工时、成本、资源调配
- **跟踪**：基线 0–10、完成百分比、挣值、关键路径、延迟/可宽延显示
- **视图**：甘特图、日历、网络图、日程表、任务窗体；分组、筛选、突出显示、大纲数字
- **工作日历**：中国法定节假日与调休，自定义日历
- **客户里程碑**：选主机厂，勾选节点并填日期，插入为固定里程碑
- **默认模板**：客户里程碑占位 + PMBOK 五大过程组（启动 / 规划 / 执行 / 监控 / 收尾）
- **导入**：MS Project XML、MPP（Project 2007–2024 的 .mpp 在浏览器内离线解析；更早版本经转换服务）、GanttProject .gan / CSV、JSON
- **导出**：PDF / JPG（MS Project 打印样式）、XML、GanttProject .gan、CSV、Excel、JSON
- **操作**：Ribbon 功能区、快速访问工具栏、右键菜单、撤销/重做、快捷键（F1 查看）

### 最近更新

- 2026-10-14：.mpp 可离线直接导入（浏览器内解析，无需联网）
- 2026-10-13：打开页面时可选「继续上次项目 / 新建项目 / 导入文件」；「项目」页签移到「格式」之后；客户里程碑可不选主机厂、自己填写名称和日期；README 增加英文、德文说明
- 2026-10-13：默认模板最上方加入「客户里程碑」占位（名称 xxx、日期留空，选主机厂后自动替换）；任务模式列默认隐藏
- 2026-10-12：默认模板改为 PMBOK 五大过程组（22 项任务与里程碑，已连好依赖）
- 2026-10-12：撤销前新增「⌫ 清除」一键清空（可撤销）；「文本样式」对话框、「移动 ▾」显示修正
- 2026-10-12：工具定名 ProjectPilot，根地址直接打开；macOS 风格界面；所有对话框可按 Esc 关闭

数据只保存在本机浏览器，与 OEM-Gantt 互不影响。

## English

A project scheduling tool (tasks, resources, progress tracking) modelled on MS Project / GanttProject. Single-page app; all data stays in your browser. UI in Chinese / English / German, with light / dark / system themes.

### Features

- **Tasks**: summary groups, milestones, manual/auto scheduling, FS/SS/FF/SF links with lag, constraints, deadlines, inactive and recurring tasks, notes and hyperlinks
- **Resources & cost**: resource sheet, assignments, work, cost, leveling
- **Tracking**: baselines 0–10, % complete, earned value, critical path, late tasks / slack
- **Views**: Gantt, calendar, network diagram, timeline, task form; group by, filters, highlight, outline numbers
- **Calendars**: Chinese public holidays and make-up workdays, custom calendars
- **Customer milestones**: pick an OEM, tick its milestones and enter dates; inserted as fixed milestones
- **Default template**: customer-milestone placeholders + PMBOK 5 process groups (Initiating / Planning / Executing / Monitoring / Closing)
- **Import**: MS Project XML, MPP (Project 2007–2024 .mpp files are parsed offline in the browser; older versions via conversion service), GanttProject .gan / CSV, JSON
- **Export**: PDF / JPG (MS Project print style), XML, GanttProject .gan, CSV, Excel, JSON
- **Usability**: ribbon, Quick Access Toolbar, context menu, undo/redo, keyboard shortcuts (press F1)

Data is stored only in your browser and is separate from OEM-Gantt.

## Deutsch

Ein Projektplanungswerkzeug (Vorgänge, Ressourcen, Fortschrittsverfolgung) nach dem Vorbild von MS Project / GanttProject. Single-Page-App; alle Daten bleiben im Browser. Oberfläche auf Chinesisch / Englisch / Deutsch, mit hellem / dunklem / System-Design.

### Funktionen

- **Vorgänge**: Sammelvorgänge, Meilensteine, manuelle/automatische Planung, EA/AA/EE/AE-Verknüpfungen mit Zeitabstand, Einschränkungen, Stichtage, inaktive und periodische Vorgänge, Notizen und Hyperlinks
- **Ressourcen & Kosten**: Ressourcentabelle, Zuordnungen, Arbeit, Kosten, Kapazitätsabgleich
- **Überwachung**: Basispläne 0–10, % abgeschlossen, Ertragswert, kritischer Pfad, verspätete Vorgänge / Puffer
- **Ansichten**: Gantt, Kalender, Netzplan, Zeitachse, Vorgangsmaske; Gruppieren, Filter, Hervorheben, Gliederungsnummern
- **Kalender**: chinesische Feiertage und Ersatzarbeitstage, eigene Kalender
- **Kundenmeilensteine**: OEM wählen, Meilensteine ankreuzen und Termine eintragen; werden als feste Meilensteine eingefügt
- **Standardvorlage**: Platzhalter für Kundenmeilensteine + PMBOK-5-Prozessgruppen (Initiierung / Planung / Ausführung / Überwachung / Abschluss)
- **Import**: MS Project XML, MPP (.mpp aus Project 2007–2024 wird offline im Browser gelesen; ältere Versionen über Konvertierungsdienst), GanttProject .gan / CSV, JSON
- **Export**: PDF / JPG (MS-Project-Druckstil), XML, GanttProject .gan, CSV, Excel, JSON
- **Bedienung**: Menüband, Symbolleiste für den Schnellzugriff, Kontextmenü, Rückgängig/Wiederholen, Tastenkürzel (F1)

Daten werden nur im Browser gespeichert und sind von OEM-Gantt getrennt.
