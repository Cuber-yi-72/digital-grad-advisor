# 上游登记表（永不删除）

沙箱存储有上限。`vendor/` 可整夹删；**URL 只写在本表**。改造层 `SKILL.md` 只保留 `REGISTRY id：…` 一行。拉取后的 commit 见 `skills/LOCKS.md`。

系统提示词**不**存放这些链接，以免占常驻上下文。拉取只读本表 + `skills/sync-upstream/SKILL.md`。回收只读 `skills/gc-storage/SKILL.md`。

使用记录写 `skills/USAGE.md`（可被 GC 截断，但不要删文件本身）。

---

## 禁止回收（直到工作区只剩这些）

- `00-核心/` `01-配置/` `AGENTS.md` `README.md` `使用手册.md`
- **本文件** `skills/REGISTRY.md`
- `skills/sync-upstream/SKILL.md` `skills/gc-storage/SKILL.md` `skills/profile-update/SKILL.md`
- `scripts/sync-upstream.py` `scripts/sync-upstream.sh`
- 改造层 `skills/*/SKILL.md`（默认禁止回收。§4 仅当用户明确同意 **且** 本工具包已有 git remote 才可删；**无 remote 则拒绝删**——zip 交付默认没有 remote，删了就回不来）

## 可回收，且必须能按 URL 重拉

`can_evict: vendor`。删除后本地目录可以不存在；需要时 `git clone --depth 1 <repo>`，再拷 `<from>` 到 `<local>`。

| id | 何时 | repo | from（仓库内） | local（删了就重拉） | license |
|----|------|------|----------------|---------------------|---------|
| phd.literature-research | 文献检索链 | https://github.com/fcakyon/phd-skills | plugin/skills/literature-research | vendor/phd-skills/literature-research | MIT |
| phd.experiment-design | 消融矩阵 | https://github.com/fcakyon/phd-skills | plugin/skills/experiment-design | vendor/phd-skills/experiment-design | MIT |
| phd.paper-writing | 论文各节 | https://github.com/fcakyon/phd-skills | plugin/skills/paper-writing | vendor/phd-skills/paper-writing | MIT |
| phd.reviewer-defense | 审稿防御 | https://github.com/fcakyon/phd-skills | plugin/skills/reviewer-defense | vendor/phd-skills/reviewer-defense | MIT |
| phd.debug | 失败诊断 | https://github.com/fcakyon/phd-skills | plugin/skills/debug | vendor/phd-skills/debug | MIT |
| phd.paper-verification | 核稿 | https://github.com/fcakyon/phd-skills | plugin/skills/paper-verification | vendor/phd-skills/paper-verification | MIT |
| phd.reproduce | 复现 | https://github.com/fcakyon/phd-skills | plugin/skills/reproduce | vendor/phd-skills/reproduce | MIT |
| sci.experimental-design | Fisher DOE | https://github.com/K-Dense-AI/scientific-agent-skills | skills/experimental-design | vendor/scientific-agent-skills/experimental-design | MIT |
| sci.literature-review | 系统综述 | https://github.com/K-Dense-AI/scientific-agent-skills | skills/literature-review | vendor/scientific-agent-skills/literature-review | MIT |
| sci.hypothesis-generation | 假设 | https://github.com/K-Dense-AI/scientific-agent-skills | skills/hypothesis-generation | vendor/scientific-agent-skills/hypothesis-generation | MIT |
| sci.statistical-power | 功效 | https://github.com/K-Dense-AI/scientific-agent-skills | skills/statistical-power | vendor/scientific-agent-skills/statistical-power | MIT |
| sci.peer-review | 模拟审稿 | https://github.com/K-Dense-AI/scientific-agent-skills | skills/peer-review | vendor/scientific-agent-skills/peer-review | MIT |
| sci.citation-management | 引用核验 | https://github.com/K-Dense-AI/scientific-agent-skills | skills/citation-management | vendor/scientific-agent-skills/citation-management | MIT |
| pptx.academic | 组会/答辩幻灯片 | https://github.com/Gabberflast/academic-pptx-skill | . (SKILL.md, content_guidelines.md, slide_patterns.md, README.md) | vendor/academic-pptx-skill | MIT |

每个上游仓库的 LICENSE 随拷贝放在 `vendor/<包>/`。删 vendor 时 LICENSE 可一起删，重拉时再拷。

## 不进 vendor（插件，不占本沙箱）

| id | repo | license | 安装 |
|----|------|---------|------|
| ars | https://github.com/Imbad0202/academic-research-skills | CC BY-NC 4.0 | `/plugin marketplace add Imbad0202/academic-research-skills` |

## 改造层 ↔ 上游 id（删 vendor 后仍知道拉谁）

| 改造层（勿轻易删） | 需要的 REGISTRY id |
|--------------------|-------------------|
| literature-review | phd.literature-research, sci.literature-review, sci.citation-management |
| topic-and-proposal | sci.hypothesis-generation |
| experiment-design | sci.experimental-design, sci.statistical-power, phd.experiment-design |
| research-execution | phd.debug, phd.reproduce |
| paper-writing | phd.paper-writing, sci.citation-management, phd.paper-verification |
| paper-review-rebuttal | phd.reviewer-defense, sci.peer-review |
| weekly-meeting, grad-life, thesis-and-defense | pptx.academic |
| literature-review / topic-and-proposal（可选） | ars（插件，不进 vendor） |

拉新包：MIT/Apache 才进 `vendor/`；NC 只插件安装。加 id 只改本表，`scripts/sync-upstream.py` 按表拉取，不要在脚本里写死 skill 名。
