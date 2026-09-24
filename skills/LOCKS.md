# 上游锁定（sync-upstream 成功后自动改）

SHA 由 `scripts/sync-upstream.sh` 自动维护。空表 = 尚未拉取。重拉前对比 SHA，变了要扫 REGISTRY 的 `from` 路径是否仍存在。

| repo | sha | pulled_at_utc | note |
|------|-----|----------------|------|
