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
- **默认模板**：客户里程碑占位 + APQP 五大过程（计划和确定项目 / 产品设计和开发 / 过程设计和开发 / 产品和过程确认 / 反馈、评定和纠正措施）
- **导入**：MS Project XML、MPP（Project 2007–2024 的 .mpp 在浏览器内离线解析；更早版本经转换服务）、GanttProject .gan / CSV、JSON
- **导出**：PDF / JPG（MS Project 打印样式）、XML、GanttProject .gan、CSV、Excel（.xlsx，甘特色块随日期自动变化）、JSON
- **操作**：Ribbon 功能区（可切回旧版布局）、快速访问工具栏、右键菜单、撤销/重做、快捷键（F1 查看）

### 最近更新

- 2026-10-16（1.2.0）：导出 Excel 改为 .xlsx，甘特色块用条件格式生成，在 Excel 里改开始/结束日期，色块和分组起止自动跟着变
- 2026-10-15（1.1.0）：功能区重排——文件页加入新建/打开/保存，常用导入导出平铺；字体移到格式页；显示选项直接勾选；视图页不再重复资源/报表按钮；图标按钮加文字。可在「文件 › 帮助 › 旧版功能区」一键切回，旧版在线地址 /v1.0/
- 2026-10-15：导出前弹出确认框，可选择保存到哪个文件夹（Chrome/Edge）
- 2026-10-15：客户里程碑选 BMW 时，节点 2、3、7、8、9、11、12 默认不勾选
- 2026-10-14：默认模板改为 APQP 五大过程（35 项任务与里程碑，已连好依赖），未改名的阶段和任务随语言切换

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
- **Default template**: customer-milestone placeholders + APQP 5 phases (Plan & Define / Product Design / Process Design / Validation / Feedback & Corrective Action)
- **Import**: MS Project XML, MPP (Project 2007–2024 .mpp files are parsed offline in the browser; older versions via conversion service), GanttProject .gan / CSV, JSON
- **Export**: PDF / JPG (MS Project print style), XML, GanttProject .gan, CSV, Excel (.xlsx, Gantt bars update automatically when dates change), JSON
- **Usability**: ribbon (classic layout switchable), Quick Access Toolbar, context menu, undo/redo, keyboard shortcuts (press F1)

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
- **Standardvorlage**: Platzhalter für Kundenmeilensteine + APQP mit 5 Phasen (Planung / Produktentwicklung / Prozessentwicklung / Validierung / Rückmeldung)
- **Import**: MS Project XML, MPP (.mpp aus Project 2007–2024 wird offline im Browser gelesen; ältere Versionen über Konvertierungsdienst), GanttProject .gan / CSV, JSON
- **Export**: PDF / JPG (MS-Project-Druckstil), XML, GanttProject .gan, CSV, Excel (.xlsx, Balken passen sich bei Datumsänderung automatisch an), JSON
- **Bedienung**: Menüband (klassisches Layout umschaltbar), Symbolleiste für den Schnellzugriff, Kontextmenü, Rückgängig/Wiederholen, Tastenkürzel (F1)

Daten werden nur im Browser gespeichert und sind von OEM-Gantt getrennt.
