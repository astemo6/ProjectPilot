# mpp2xml — .mpp 在线导入服务

用 [MPXJ](https://www.mpxj.org/) 把 Microsoft Project `.mpp/.mpt/.mpx` 等文件转换成 MSPDI XML，甘特图前端再按 XML 导入。

- `POST /convert`：multipart 字段 `file`（或原始字节），返回 MSPDI XML
- `GET /health`
- 不保存文件：临时文件转换完立即删除，不记录访问日志
- 限制：单文件 30 MB、每 IP 每分钟 20 次，CORS 只允许 `https://astemo6.github.io`

## 部署（Docker）

```bash
cd /opt/docker/mpp2xml
docker compose up -d --build
```

Caddy 用 sslip.io 域名自动申请 Let's Encrypt 证书，HTTPS 走 8443（443 已被占用），80 端口仅用于证书验证。
公开地址：`https://mpp.45-92-159-155.sslip.io:8443/convert`
