# Skills 索引

每个子目录是一个 [Agent Skills](https://agentskills.io) 包：`name` 与文件夹名相同，`description` 供 Agent 路由。

部署：将本 `skills/` 目录复制到 `.cursor/skills/`、`.claude/skills/` 或 `.agents/skills/`。ChatGPT / Claude Project 则把需要的 `SKILL.md` 当作知识文件上传。

| Skill | 何时用 | 学生可能说的话 |
|-------|--------|----------------|
| `grad-life` | **生涯主线**：怎么学、怎么汇报、组会、能力成长 | 不会当研究生；组会怕；没进展怎么报 |
| `onboarding-and-courses` | 入学、选课、专业课、补基础、进组 | 培养方案怎么看；跨考高等数学忘光了 |
| `literature-review` | 检索、精读、综述、文献管理 | 不会读英文论文；综述不知道怎么组织 |
| `topic-and-proposal` | 选题、问题定义、开题 | 导师让我做这个但没创新；开题答辩怕被问 |
| `experiment-design` | 实验/工艺/表征/仿真方案 | 正交怎么排；仿真和实验怎么对 |
| `research-execution` | 执行、失败诊断、记录、周计划；中期用模板 `03-模板/中期考核.md` | 重复不出来；这周白做了；下个月中期 |
| `paper-writing` | 会议/期刊论文 | Introduction 不会写；图不知道取舍 |
| `paper-review-rebuttal` | 投稿、返修 | 审稿人互相矛盾；cover letter |
| `patent-and-ip` | 专利时序、交底 | 先发论文还是先申请；交底书不会写 |
| `thesis-and-defense` | 大论文、答辩 | 大论文和已发表小论文怎么拼 |
| `weekly-meeting` | 周报、组会 PPT、一对一、听会提问 | 导师总说我没进展；标题怎么写 |
| `idp-and-career` | 去向与 IDP（怎么当研究生见 grad-life） | 要不要读博；秋招和实验冲突 |
| `integrity-and-wellbeing` | 诚信、安全、压力、关系 | 查重；想退学；和导师聊不了 |
| `profile-update` | 改导师/学生/实验室活标签 | 老师其实刀子嘴豆腐心；标签错了 |
| `sync-upstream` | 按 REGISTRY 从 GitHub 按需拉 vendor | 拉取上游；vendor 被回收了 |
| `gc-storage` | 沙箱满了先删旧文件再删不用的 vendor | 空间不够；清理文件 |

配置、USAGE、无 vendor、回收：**只写在 `AGENTS.md`**。有上游的 skill 文末仅一行 `REGISTRY id：…`；对照表在 `REGISTRY.md`。无 vendor 用改造层就地方法。冲突以不代写、安全、专利、真人导师拍板为准。