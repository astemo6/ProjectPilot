import json,os,re
W='/workspace/work'; O=W+'/offline/ProjectPilot-离线版'; os.makedirs(O,exist_ok=True)
def inl(html,wc): return html.replace('<script src="workcal.js"></script>','<script>'+wc+'</script>')
wc4=open(W+'/gt4/workcal.js').read(); wc3=open(W+'/gt3/workcal.js').read()
pp=inl(open(W+'/gt4/index.html').read(),wc4)
assert '<script src="workcal.js">' not in pp
pp=pp.replace('id="lnkOem" href="oem/"','id="lnkOem" href="OEM-Gantt.html"')
open(O+'/ProjectPilot.html','w').write(pp)
plan=inl(open(W+'/gt3/plan.html').read(),wc3)
plan=plan.replace('new URL(location.href)','new URL(window.__OFFLINE_URL || location.href)').replace("history.replaceState(null, '', u.toString());","if(!window.__OFFLINE_URL) history.replaceState(null, '', u.toString());")
sh=open(W+'/gt3/index.html').read()
sh=sh.replace('href="../" data-t="toV4"','href="ProjectPilot.html" data-t="toV4"')
inj='<script>window.__OFFLINE_PLAN__='+json.dumps(plan).replace('</','<\\/')+';</script>\n'
k=sh.index('<script>'); sh=sh[:k]+inj+sh[k:]
open(O+'/OEM-Gantt.html','w').write(sh)
open(O+'/使用说明.txt','w',encoding='utf-8').write('ProjectPilot 离线版（无需安装、无 exe）\r\n\r\n1. 解压到任意文件夹。\r\n2. 用 Edge 或 Chrome 打开 ProjectPilot.html（可右键 → 打开方式 → Microsoft Edge）。\r\n3. 右上角「OEM-Gantt ↗」打开主机厂节点图（OEM-Gantt.html）。\r\n4. 数据保存在该浏览器里，与网页版数据互不相通；用「文件 → 导出/导入」转移或备份。\r\n5. 导入 .mpp：电脑联网即可直接导入；完全断网时，请在 MS Project 里「另存为 → XML」，再导入 .xml 文件。\r\n')
print(os.listdir(O))
