---
name: paper-review-rebuttal
description: 投稿前预审、审稿意见拆解与返修。改造自 phd-skills/reviewer-defense 与 scientific-agent-skills/peer-review。学生说投稿、cover letter、返修、审稿人、major revision、模拟审稿时使用。
---

# 预审与返修 · 改造层（工科导师）

## 必读上游

1. `vendor/phd-skills/reviewer-defense/SKILL.md`  
   脆弱点分析（技术/呈现/实验）→ 按 venue 文化预判 → ≥10 个可能问题（可不可用现有数据答）→ 消融子集选择 → 阴性结果怎么讲 → 真返修时先读完全部意见。
2. `vendor/scientific-agent-skills/peer-review/SKILL.md`  
   作正式模拟审稿时用其结构。语气专业；总体评价必须与优缺点一致。

把上游「CVPR/NeurIPS」换成工科常见：领域学会会议、IEEE/Elsevier 应用刊、中文核心（仅当培养方案认）。期刊比会议更抠相关工作与可重复。无 vendor：仍做意见分类表、补实验闸门、点对点回复骨架；不伪造已做实验。

## 导师叠加

### 投稿前

故事线与图自洽；作者名单以导师最终为准；Cover letter 四段；不编审稿人邮箱。

### 拆意见表

序号 | 审稿人 | 类型(事实错误/缺实验/缺引用/口味/致命) | 决策(改稿/补实验/解释不改/问导师)

互斥意见：选与证据一致的一侧，不要两头讨好导致逻辑裂。

补实验只补能改结论的。时间不够：缩主张或导师出面延期。不伪造「已经补做」。

### 回复信

开场感谢 + 改动总览。每条：Comment 原文 → Response → 稿件改动位置。不讽刺审稿人。致命且属实：建议改主张或换刊，不教糊弄。

拒稿：吸收后换刊；禁止一稿多投。

## 输出

弱点表 | Top 问题（含是否现有数据可答） | 补实验是否值得 | 回复骨架（学生填证据） | 需导师确认

REGISTRY id：phd.reviewer-defense · sci.peer-review
