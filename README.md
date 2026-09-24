# 工科数字研究生导师

给**真人导师**用的 AI Agent 工具包：用 prompt engineering + 标准 Agent Skills，把你对研究生「事无巨细」的指导，变成可复用、可部署、可定制的数字导师。

面向：**材料 / 电子 / 机电等工程学科**（实验、表征、工艺、仿真、专利与论文并重）。  
交互语言：**中文**。论文、投稿信、审稿回复可中英对照。

> 定位一句话：**补位不替代。** 数字导师负责日常陪练、结构化思考、质量检查和下一步拆解；方向拍板、经费、署名、送审、毕业资格，仍由真人导师决定。

---

## 你得到什么

| 模块 | 作用 |
|------|------|
| [00-核心/SYSTEM.md](00-核心/SYSTEM.md) | 完整系统提示词（人设、原则、阶段感知、输出格式） |
| [00-核心/边界与红线.md](00-核心/边界与红线.md) | 学术诚信、安全、心理、署名等不可逾越的规则 |
| [01-配置/](01-配置/) | 实验室/学生档案、**可改的标签与证据**、培养时间线 |
| [skills/](skills/) | 改造层 `SKILL.md`；上游 **GitHub 地址只写在** [skills/REGISTRY.md](skills/REGISTRY.md)（本包默认不带 `vendor/`，按需拉） |
| [03-模板/](03-模板/) | 周报、文献矩阵、实验记录、IDP、开题骨架等可直接发给学生的表格 |
| [使用手册.md](使用手册.md) | ChatGPT Custom GPT / Claude Project / Cursor / Claude Code 部署步骤 |
| [AGENTS.md](AGENTS.md) | 放进仓库根目录即可被 Cursor、Codex、Claude Code 读取 |

学生不需要会 prompt。他们用自然语言说「这周实验全失败了」「开题不知道怎么写创新点」，Agent 会按 skill 的工作流来带。

---

## 研究生全周期覆盖

```
录取前后 ──► 入学适应 / 选课 / 实验室融入
                │
                ▼
         文献与方向扫描 ──► 选题 / 开题
                │
                ▼
         实验设计 / 执行 / 失败诊断 / 实验记录
                │
                ├──► 会议论文 / 期刊
                ├──► 专利挖掘与申请时序
                └──► 中期考核
                │
                ▼
         学位论文 / 答辩 / 就业或升学
```

对应 skills（文件夹名 = 斜杠命令名）：

1. `grad-life` — **从入学怎么学、怎么汇报、组会注意什么**（生涯主线）
2. `onboarding-and-courses` — 培养方案、选课、专业课
3. `literature-review` — 检索、精读、文献矩阵、综述
4. `topic-and-proposal` — 选题、问题定义、开题报告
5. `experiment-design` — 实验/工艺/表征/仿真设计
6. `research-execution` — 周计划、失败诊断、实验记录
7. `paper-writing` — 会议/期刊论文
8. `paper-review-rebuttal` — 投稿、返修
9. `patent-and-ip` — 专利时序与交底
10. `thesis-and-defense` — 学位论文与答辩
11. `weekly-meeting` — 周报、组会 PPT、一对一
12. `idp-and-career` — 读博/就业/出国
13. `integrity-and-wellbeing` — 学术规范、安全、压力
14. `profile-update` — 按对话证据更新导师/学生标签
15. `sync-upstream` — 按 `skills/REGISTRY.md` 从 GitHub 按需重拉
16. `gc-storage` — 空间满时回收；GitHub 链接留在登记表不放系统提示词

学生先读 [03-模板/研究生生涯手册.md](03-模板/研究生生涯手册.md)。索引见 [skills/README.md](skills/README.md)。

---

## 10 分钟快速开始

1. 打开 [00-核心/SYSTEM.md](00-核心/SYSTEM.md)，整份复制为系统提示词。Agent 会先问清你是学生还是导师、几年级、本周卡在哪。
2. 填写 [01-配置/实验室档案.md](01-配置/实验室档案.md)（课题组方向、设备、投稿习惯、你的风格）。
3. 给学生一份 [01-配置/学生档案.md](01-配置/学生档案.md)，让每人填完贴进对话。
4. 按 [使用手册.md](使用手册.md) 部署到你常用的模型。
5. 需要深度任务时，把对应 `skills/<name>/SKILL.md` 作为知识文件上传，或拷到 `.cursor/skills/`。

定制优先级：**实验室档案 > 系统提示词里的「导师风格」段 > 单个 skill**。先填档案，比改 prompt 更有效。

发给学生之前：请你自己 `git init` 并推到**私有**远端。zip 里没有 git remote；没有 remote 时回收规则会拒绝删除改造层（删了回不来）。

---

## 学术方法从哪来

本包**不内嵌**上游仓库。需要文献链 / DOE / 审稿 / 幻灯片时，Agent 按 [skills/REGISTRY.md](skills/REGISTRY.md) 从 GitHub 按需拉取。地址不写在系统提示词里。

红线对学生公开：[00-核心/边界与红线.md](00-核心/边界与红线.md)。