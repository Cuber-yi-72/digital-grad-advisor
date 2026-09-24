---
name: gc-storage
description: 沙箱存储或文件数接近上限时回收。先删很久以前的不重要用户文件，再删不常用的 vendor 上游 skills；登记表与 GitHub 链接必须留下以便重拉。在用户说空间不够、文件太多、清理、或你观察到工作区膨胀时使用。
---

# 存储回收

沙箱快照通常有体积/文件数上限。回收是为了继续对话。

**GitHub 地址只在 `skills/REGISTRY.md`。** 改造层只留 `REGISTRY id` 一行。删 vendor 后按登记表重拉。

## 0. 平台分支（先看有没有 shell）

**无文件系统 / 无 shell**（ChatGPT Custom GPT、Claude Project、粘贴对话）：

- **不要**跑 `du`、`find`、`rm`，不要声称已经删了文件。
- 只输出一份回收清单：建议删什么、为什么、删了以后如何按 REGISTRY 重拉。
- IRON 按 AGENTS：回复末尾给一行待粘贴的 USAGE 记录，由用户自己写入。

**有 shell** 才执行下面 §1–4。先 `du -sh` 与 `find … | wc -l` 看占用，能 dry-run 先列出将删路径。USAGE 若从未落盘（用户一直在无 shell 环境），**不得**把「USAGE 全空」当成「所有 vendor 从未使用」而批量删——改为问用户最近在用哪些 id。

## 触发

- 用户说清理、空间满、文件太多
- 工作区接近平台上限（体积或文件数）
- 将要 clone 上游但空间不够

## 优先级（先 1 后 4）

### 1. 很久以前、且不重要的投递文件

删：重复 PDF、截图、导出、`Unselected files/`、明显一次性的作业草稿、`/tmp`、`__pycache__`、完整 git clone 缓存（如仓库外的 `_vendor/`）。

不删：当前学生档案、本周周报、标签与证据、实验室档案、正在改的开题。

「很久」：超过 14 天未在 USAGE 或对话中点名，且用户未说「留着」。有疑先问一句；用户已说「清空间」则按表执行并列出清单。

### 2. 不常用的上游 vendor skills

只删 `vendor/**` 中 USAGE 里最久未用、或从未出现的 REGISTRY id 对应目录。

**删目录前确认** `skills/REGISTRY.md` 已有该 id 的 repo + from + local。没有就先补登记再删。

可以同时删整个 `vendor/phd-skills/<skill>`，保留 `vendor/phd-skills/LICENSE` 直到该包最后一个 skill 也被删。

默认不删改造层 `skills/<name>/SKILL.md`。经用户明确同意才可按 §4。

### 3. 仍不够：整包 vendor

可 `rm -rf vendor/phd-skills vendor/scientific-agent-skills vendor/academic-pptx-skill`。REGISTRY 仍在，下次任务走 `sync-upstream` 按需只拉一个 id，不要一次再 clone 全家桶。

### 4. 最后才碰改造层

只有空间仍然不够、**且用户明确同意**，才删长期不用的改造层文件夹。

改造层不在上游 GitHub。§4 的恢复前提是**本工具包自己的 git remote**。因此：

- 工作区没有 `git remote`（当前 zip 交付默认如此）→ **拒绝删改造层**，改请用户外迁大文件或先自己 `git init` 并推到私有远端。
- 有 remote 且用户同意：删完在 REGISTRY 底部「已卸载改造层」写下名字。

## 永远不删

`skills/REGISTRY.md` · `skills/gc-storage/SKILL.md` · `skills/sync-upstream/SKILL.md` · `00-核心/` · `01-配置/` · `AGENTS.md` · `LICENSE` · `scripts/sync-upstream.py` · `scripts/sync-upstream.sh` · `scripts/validate.py`

## 删完

在回复列出：删了什么、腾出多少、哪些 id 现为「本地缺失，URL 仍在 REGISTRY」。需要其中某一个时立即 `sync-upstream`，不要让用户手抄链接。

有文件系统：追加 USAGE 一行。若 USAGE 过长，先 `python3` 或 `python scripts/compact-usage.py`（每 id 保留最后一行），再按「最久未用」删 vendor。无文件系统：只给待粘贴的一行。

截断后没有某 id 的行 = 视为从未使用，可优先回收其 vendor，**不得**把「被截掉的唯一记录」当成还在用。
