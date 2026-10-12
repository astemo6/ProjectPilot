/* workcal.js — 计划页与执行页共用的工作日历（window.WORKCAL）
   mode: "CN" 中国（周末 + 法定节假日 + 调休） | "DE" 德国（周末 + 全国性法定假日） | "WE" 仅周末 | "OFF" 自然日
   cal = { mode, holidays:{ "YYYY-MM-DD": 名称 }, makeup:{ "YYYY-MM-DD": 1 } }
   holidays / makeup 是可编辑层：CN 模式默认预填国务院公布的节假日；任何模式下都可追加自定义放假/补班。 */
(function (root) {
  "use strict";
  var KEY = "gantt-workcal-v1";
  var CN = {
    2026: {
      hol: [["2026-01-01", "2026-01-03", "元旦"], ["2026-02-15", "2026-02-23", "春节"], ["2026-04-04", "2026-04-06", "清明"], ["2026-05-01", "2026-05-05", "劳动节"],
            ["2026-06-19", "2026-06-21", "端午"], ["2026-09-25", "2026-09-27", "中秋"], ["2026-10-01", "2026-10-07", "国庆"]],
      mk: ["2026-01-04", "2026-02-14", "2026-02-28", "2026-05-09", "2026-09-20", "2026-10-10"]
    }
  };
  function pad(n) { return (n < 10 ? "0" : "") + n; }
  function iso(d) { return d.getFullYear() + "-" + pad(d.getMonth() + 1) + "-" + pad(d.getDate()); }
  function parse(s) { var p = String(s).split("-"); return new Date(+p[0], +p[1] - 1, +p[2]); }
  function easter(y) {
    var a = y % 19, b = Math.floor(y / 100), c = y % 100, d = Math.floor(b / 4), e = b % 4, f = Math.floor((b + 8) / 25), g = Math.floor((b - f + 1) / 3);
    var h = (19 * a + b - d - g + 15) % 30, i = Math.floor(c / 4), k = c % 4, l = (32 + 2 * e + 2 * i - h - k) % 7, m = Math.floor((a + 11 * h + 22 * l) / 451);
    return new Date(y, Math.floor((h + l - 7 * m + 114) / 31) - 1, ((h + l - 7 * m + 114) % 31) + 1);
  }
  var DE_CACHE = {};
  /* 德国全国性法定假日（各州假日不含） */
  function deHolidays(y) {
    if (DE_CACHE[y]) return DE_CACHE[y];
    var o = {}, e = easter(y);
    function add(d, n) { o[iso(d)] = n; }
    function off(n) { var d = new Date(e); d.setDate(d.getDate() + n); return d; }
    add(new Date(y, 0, 1), "Neujahr"); add(off(-2), "Karfreitag"); add(off(1), "Ostermontag"); add(new Date(y, 4, 1), "Tag der Arbeit");
    add(off(39), "Christi Himmelfahrt"); add(off(50), "Pfingstmontag"); add(new Date(y, 9, 3), "Tag der Deutschen Einheit");
    add(new Date(y, 11, 25), "1. Weihnachtstag"); add(new Date(y, 11, 26), "2. Weihnachtstag");
    return (DE_CACHE[y] = o);
  }
  /* CN 模式的默认可编辑层 */
  function cnDefaults() {
    var h = {}, m = {};
    Object.keys(CN).forEach(function (y) {
      CN[y].hol.forEach(function (r) { var d = parse(r[0]), e = parse(r[1]), g = 0; while (d <= e && g++ < 60) { h[iso(d)] = r[2]; d.setDate(d.getDate() + 1); } });
      CN[y].mk.forEach(function (s) { m[s] = 1; });
    });
    return { holidays: h, makeup: m };
  }
  function defaults(mode) {
    mode = mode || "CN";
    var c = mode === "CN" ? cnDefaults() : { holidays: {}, makeup: {} };
    c.mode = mode; return c;
  }
  function norm(c) {
    if (!c || typeof c !== "object") return defaults("CN");
    var mode = { CN: 1, WE: 1, OFF: 1 }[c.mode] ? c.mode : "CN"; /* 德国日历已移除（2026-10-11），旧数据 DE → CN */
    var mk = c.makeup || {};
    if (Array.isArray(mk)) { var o = {}; mk.forEach(function (s) { o[s] = 1; }); mk = o; }
    return { mode: mode, holidays: c.holidays && typeof c.holidays === "object" ? c.holidays : {}, makeup: mk };
  }
  function load() {
    try { var s = root.localStorage.getItem(KEY); if (s) return norm(JSON.parse(s)); } catch (e) {}
    return defaults("CN");
  }
  function save(c) { try { root.localStorage.setItem(KEY, JSON.stringify({ mode: c.mode, holidays: c.holidays, makeup: Object.keys(c.makeup || {}) })); return true; } catch (e) { return false; } }
  /* s: "YYYY-MM-DD" 或 Date */
  function isWork(s, c) {
    if (typeof s !== "string") s = iso(s);
    if (!c || c.mode === "OFF") return true;
    if (c.makeup[s]) return true;
    if (c.holidays[s]) return false;
    if (c.mode === "DE" && deHolidays(+s.slice(0, 4))[s]) return false;
    var w = parse(s).getDay(); return w !== 0 && w !== 6;
  }
  function holName(s, c) {
    if (typeof s !== "string") s = iso(s);
    if (!c || c.mode === "OFF" || c.makeup[s]) return "";
    if (c.holidays[s]) return typeof c.holidays[s] === "string" ? c.holidays[s] : "假日";
    if (c.mode === "DE") return deHolidays(+s.slice(0, 4))[s] || "";
    return "";
  }
  /* 起点向后、终点向前吸附到工作日（终点早于起点时取起点） */
  function snapRange(a, b, c) {
    var s = parse(a), e = parse(b), g = 0;
    while (!isWork(s, c) && g++ < 400) s.setDate(s.getDate() + 1);
    g = 0; while (!isWork(e, c) && g++ < 400) e.setDate(e.getDate() - 1);
    if (e < s) e = new Date(s);
    return { s: iso(s), e: iso(e) };
  }
  var NOTE = {
    zh: { CN: "内置 2026 年国务院节假日安排；其他年份仅剔除周末，可自行补充", DE: "德国全国性法定假日（自动计算复活节相关假日，不含各州假日）", WE: "仅剔除周六周日", OFF: "关闭：工期按自然日计算" },
    en: { CN: "Built-in 2026 China holiday schedule; other years exclude weekends only", DE: "German nationwide public holidays (state holidays not included)", WE: "Saturdays and Sundays only", OFF: "Off: durations count calendar days" },
    de: { CN: "Chinesischer Feiertagsplan 2026 integriert; andere Jahre nur Wochenenden", DE: "Bundesweite Feiertage (ohne Landesfeiertage)", WE: "Nur Samstage und Sonntage", OFF: "Aus: Dauer in Kalendertagen" }
  };
  var LABEL = {
    zh: { CN: "中国（法定节假日+调休）", DE: "德国（全国性假日）", WE: "仅周末", OFF: "关闭（自然日）" },
    en: { CN: "China (holidays + make-up days)", DE: "Germany (nationwide)", WE: "Weekends only", OFF: "Off (calendar days)" },
    de: { CN: "China (Feiertage + Ausgleichstage)", DE: "Deutschland (bundesweit)", WE: "Nur Wochenenden", OFF: "Aus (Kalendertage)" }
  };
  root.WORKCAL = { KEY: KEY, CN: CN, defaults: defaults, norm: norm, load: load, save: save, isWork: isWork, holName: holName, snapRange: snapRange, deHolidays: deHolidays, NOTE: NOTE, LABEL: LABEL, iso: iso, parse: parse };
})(typeof window !== "undefined" ? window : globalThis);
