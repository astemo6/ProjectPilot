"""MPP → MSPDI XML 转换服务（MPXJ）。POST /convert ，请求体为文件原始字节（或 multipart 字段 file）。"""
import os, tempfile, time, threading, cgi, io, json
from http.server import ThreadingHTTPServer, BaseHTTPRequestHandler
import jpype, jpype.imports, mpxj  # noqa: F401  (mpxj 把 jar 加入 classpath)
jpype.startJVM("-Xmx512m", "-Djava.awt.headless=true")
from org.mpxj.reader import UniversalProjectReader
from org.mpxj.mspdi import MSPDIWriter

MAX = int(os.environ.get("MAX_MB", "30")) * 1024 * 1024
ORIGINS = [o.strip() for o in os.environ.get("ALLOW_ORIGINS", "*").split(",") if o.strip()]
RATE = int(os.environ.get("RATE_PER_MIN", "20"))
hits, lock = {}, threading.Lock()

def allowed(ip):
    now = time.time()
    with lock:
        q = [t for t in hits.get(ip, []) if now - t < 60]
        if len(q) >= RATE: hits[ip] = q; return False
        q.append(now); hits[ip] = q; return True

def _d(v):
    return str(v)[:19] if v is not None else ""

def add_ext(proj, xml):
    """追加两段注释（ProjectLibre/MS Project 会忽略）：展开后的日历例外（含周期性例外）和拆分任务的工作时段。"""
    cals, splits = {}, {}
    try:
        for c in proj.getCalendars():
            items = []
            for ex in c.getCalendarExceptions():
                try: lst = ex.getExpandedExceptions()
                except Exception: lst = [ex]
                for e in lst:
                    items.append([_d(e.getFromDate())[:10], _d(e.getToDate())[:10], 1 if e.getWorking() else 0, str(ex.getName() or "")])
                    if len(items) > 5000: break
            cals[str(c.getUniqueID())] = items
    except Exception: pass
    try:
        for t in proj.getTasks():
            sp = t.getWorkSplits() if hasattr(t, "getWorkSplits") else t.getSplits()
            if sp is not None and sp.size() > 1:
                splits[str(t.getUniqueID())] = [[_d(r.getStart()), _d(r.getEnd())] for r in sp]
    except Exception: pass
    tail = ""
    if cals: tail += "<!--HarkCalendars " + json.dumps(cals, ensure_ascii=False).replace("--", "- -") + "-->"
    if splits: tail += "<!--HarkSplits " + json.dumps(splits).replace("--", "- -") + "-->"
    if not tail: return xml
    i = xml.rfind(b"</Project>")
    return xml[:i] + tail.encode("utf-8") + xml[i:] if i >= 0 else xml + tail.encode("utf-8")

class H(BaseHTTPRequestHandler):
    server_version = "mpp2xml/1.0"
    def cors(self):
        o = self.headers.get("Origin", "")
        if "*" in ORIGINS: self.send_header("Access-Control-Allow-Origin", "*")
        elif o in ORIGINS: self.send_header("Access-Control-Allow-Origin", o); self.send_header("Vary", "Origin")
        self.send_header("Access-Control-Allow-Methods", "POST, GET, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type, X-Filename")
    def reply(self, code, body, ctype="application/json; charset=utf-8"):
        if isinstance(body, str): body = body.encode("utf-8")
        self.send_response(code); self.cors()
        self.send_header("Content-Type", ctype); self.send_header("Content-Length", str(len(body))); self.end_headers()
        self.wfile.write(body)
    def do_OPTIONS(self): self.send_response(204); self.cors(); self.end_headers()
    def do_GET(self):
        if self.path.rstrip("/") in ("", "/health"): self.reply(200, json.dumps({"ok": True, "service": "mpp2xml"}))
        else: self.reply(404, json.dumps({"error": "not found"}))
    def do_POST(self):
        if self.path.split("?")[0].rstrip("/") != "/convert": return self.reply(404, json.dumps({"error": "not found"}))
        ip = self.headers.get("CF-Connecting-IP") or self.headers.get("X-Forwarded-For", self.client_address[0]).split(",")[0].strip()
        if not allowed(ip): return self.reply(429, json.dumps({"error": "too many requests"}))
        n = int(self.headers.get("Content-Length") or 0)
        if n <= 0 or n > MAX: return self.reply(413, json.dumps({"error": "file too large or empty"}))
        data = self.rfile.read(n)
        ct = self.headers.get("Content-Type", "")
        if ct.startswith("multipart/form-data"):
            fs = cgi.FieldStorage(fp=io.BytesIO(data), headers=self.headers, environ={"REQUEST_METHOD": "POST", "CONTENT_TYPE": ct, "CONTENT_LENGTH": str(n)})
            if "file" not in fs: return self.reply(400, json.dumps({"error": "missing file field"}))
            data = fs["file"].file.read()
        fd, src = tempfile.mkstemp(suffix=".mpp"); os.write(fd, data); os.close(fd)
        out = src + ".xml"
        try:
            proj = UniversalProjectReader().read(src)
            if proj is None: return self.reply(415, json.dumps({"error": "unsupported file"}))
            MSPDIWriter().write(proj, out)
            with open(out, "rb") as f: xml = f.read()
            xml = add_ext(proj, xml)
            self.reply(200, xml, "application/xml; charset=utf-8")
        except Exception as e:
            self.reply(422, json.dumps({"error": "parse failed", "detail": str(e)[:300]}))
        finally:
            for p in (src, out):
                try: os.remove(p)
                except OSError: pass
    def log_message(self, fmt, *a): pass  # 不记录文件内容或来源

if __name__ == "__main__":
    ThreadingHTTPServer(("0.0.0.0", 8080), H).serve_forever()
