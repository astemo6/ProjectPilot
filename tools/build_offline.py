import json,os,re,sys
# 路径不再硬编码作者本机 /workspace/work：默认取仓库根目录，可用环境变量 OFFLINE_SRC 覆盖
# （作者本地 gt4/=主程序目录、gt3/=OEM 页目录；仓库根目录结构与之一致）
W=os.environ.get("OFFLINE_SRC") or os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def p(*a): return os.path.join(W,*a)
for f in [p('gt4','workcal.js'),p('gt4','index.html'),p('gt3','workcal.js'),p('gt3','plan.html'),p('gt3','index.html')]:
    if not os.path.exists(f): sys.exit(f"找不到 {f}：请确认 OFFLINE_SRC 指向含 gt4/、gt3/ 的工作目录，或直接在仓库根目录运行")
O=p('offline','ProjectPilot-离线版'); os.makedirs(O,exist_ok=True)
def inl(html,wc): return html.replace('<script src="workcal.js"></script>','<script>'+wc+'</script>')
wc4=open(p('gt4','workcal.js')).read(); wc3=open(p('gt3','workcal.js')).read()
pp=inl(open(p('gt4','index.html')).read(),wc4)
assert '<script src="workcal.js">' not in pp
pp=pp.replace('id="lnkOem" href="oem/"','id="lnkOem" href="OEM-Gantt.html"')
open(O+'/ProjectPilot.html','w').write(pp)
plan=inl(open(p('gt3','plan.html')).read(),wc3)
plan=plan.replace('new URL(location.href)','new URL(window.__OFFLINE_URL || location.href)').replace("history.replaceState(null, '', u.toString());","if(!window.__OFFLINE_URL) history.replaceState(null, '', u.toString());")
sh=open(p('gt3','index.html')).read()
sh=sh.replace('href="../" data-t="toV4"','href="ProjectPilot.html" data-t="toV4"')
inj='<script>window.__OFFLINE_PLAN__='+json.dumps(plan).replace('</','<\\/')+';</script>\n'
k=sh.index('<script>'); sh=sh[:k]+inj+sh[k:]
open(O+'/OEM-Gantt.html','w').write(sh)
open(O+'/使用说明.txt','w',encoding='utf-8').write('ProjectPilot 离线版（无需安装、无 exe）\r\n\r\n1. 解压到任意文件夹。\r\n2. 用 Edge 或 Chrome 打开 ProjectPilot.html（可右键 → 打开方式 → Microsoft Edge）。\r\n3. 右上角「OEM-Gantt ↗」打开主机厂节点图（OEM-Gantt.html）。\r\n4. 数据保存在该浏览器里，与网页版数据互不相通；用「文件 → 导出/导入」转移或备份。\r\n5. 导入 .mpp：Project 2007–2024 保存的 .mpp 可断网直接导入（在浏览器内解析）；更早版本（Project 2003 及以前）需联网，或在 MS Project 里「另存为 → XML」，再导入 .xml 文件。\r\n')
print(os.listdir(O))
