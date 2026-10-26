# ProjectPilot

**English** · [中文](#中文) · [Deutsch](#deutsch)

- Online / 在线地址 / Online: https://astemo6.github.io/ProjectPilot/
- OEM-Gantt（客户节点图 / customer milestone chart / Kundenmeilenstein-Diagramm）: https://astemo6.github.io/ProjectPilot/oem/

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
- **Usability**: ribbon, Quick Access Toolbar, context menu, undo/redo, keyboard shortcuts (press F1)

Data is stored only in your browser and is separate from OEM-Gantt.

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
- **操作**：Ribbon 功能区、快速访问工具栏、右键菜单、撤销/重做、快捷键（F1 查看）

### 最近更新

- 2026-10-26：「文件 → 导入 → 更多」里可填写 MPP 转换服务地址（留空用默认服务器）
- 2026-10-26：OEM-Gantt 可选「考虑节假日」，使用 ProjectPilot 的工作日历；README 改为英文、中文、德文顺序
- 2026-10-16（1.2.14）：Tesla 节点顺序调整为 DFM1 → DFM2 → Nomination
- 2026-10-16（1.2.13）：新增主机厂 Tesla(特斯拉) 客户里程碑（DFM1 → SOP+3 共 10 个节点）
- 2026-10-16（1.2.12）：删除旧版功能区（含 1.0 在线版和旧离线包）

数据只保存在本机浏览器，与 OEM-Gantt 互不影响。

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
- **Bedienung**: Menüband, Symbolleiste für den Schnellzugriff, Kontextmenü, Rückgängig/Wiederholen, Tastenkürzel (F1)

Daten werden nur im Browser gespeichert und sind von OEM-Gantt getrennt.
