---
name: sync-upstream
description: 按 skills/REGISTRY.md 从 GitHub 按需拉取上游 Agent Skills 到 vendor/。在 vendor 被 GC 删掉、本地缺失、用户说拉取或更新上游时使用。GitHub 链接以登记表为准，不写在系统提示词里。
---

# 按登记表拉取上游

**权威地址：`skills/REGISTRY.md`。** 系统提示词故意不含 URL。禁止 clone 登记表以外的陌生库当 skill。

## 何时拉

- 改造层点名的 `vendor/.../SKILL.md` 不存在（往往是 `gc-storage` 删过）
- 用户说拉取、更新上游
- 将做文献 / DOE / 组会 PPT 而对应 REGISTRY id 的 local 路径为空

无 shell：不要假装 clone。打开 REGISTRY 把该行的 repo 发给用户，或请改用带终端的环境。同时仍用改造层继续，并注明方法变粗。

## 怎么拉（按需，不要全家桶）

1. 读 REGISTRY，定位需要的 **id**（如 `sci.experimental-design`）。
2. `git clone --depth 1 <repo> /tmp/...`
3. 把 `<from>` 拷到 `<local>`，带上该包 LICENSE。
4. 不要改上游文件。
5. 只拉当前任务需要的 id。空间紧时禁止一次恢复全部 vendor。

也可以：`python3 scripts/sync-upstream.py`（或 Windows：`python scripts/sync-upstream.py`；Git Bash：`bash scripts/sync-upstream.sh`）。不带参数 = 按 REGISTRY 拉全部 vendor id；带 id = 只拉这些。空间吃紧时不要全家桶。LICENSE 或 REGISTRY `from` 路径不存在必须失败，禁止 `|| true` 吞掉。没有 `bash` 时用 py，不要以为 Windows 只能等 Git Bash。

已有目录：`pull --ff-only` 或删了重 clone，并更新 LOCKS。SHA 与 LOCKS 不一致时先检查 `from` 是否漂移。

无 shell：打开 REGISTRY 把该 id 的 repo 给用户。同时用改造层「无 vendor」段继续，禁止调用 `vendor/**/scripts`。

## 拉完

USAGE 追加一行。继续原任务。列出 id、SHA、许可。
