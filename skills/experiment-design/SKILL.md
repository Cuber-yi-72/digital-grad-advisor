---
name: experiment-design
description: 工科实验/工艺/表征/仿真设计。改造自 scientific-agent-skills/experimental-design、statistical-power 与 phd-skills/experiment-design。学生说实验方案、正交、DOE、对照、消融、表征、仿真校准时使用。
---

# 实验设计 · 改造层（工科导师）

先加载上游，再叠加材料/电子实验室约束。

## 必读上游

1. `vendor/scientific-agent-skills/experimental-design/SKILL.md`  
   Fisher 三原则：随机化、在正确层级重复、区组。设计决策树（对照比较 / 筛选 / 全因子 / 响应面 / 空间填充）。伪重复、混杂、无对照、批次效应、部分因子的别名结构。有 Python 时用  
   `vendor/scientific-agent-skills/experimental-design/scripts/doe_designs.py`、  
   `vendor/scientific-agent-skills/experimental-design/scripts/randomization.py`（seeded，可归档）。
2. `vendor/scientific-agent-skills/experimental-design/references/` 需要时再读：`factorial_and_doe.md`、`design_types.md`、`randomization_and_blocking.md`。
3. `vendor/scientific-agent-skills/statistical-power/SKILL.md` — 设计选定后再估 n。不会算就给要估的效应量、方差来源、让学生补历史数据，不编 n。
4. `vendor/phd-skills/experiment-design/SKILL.md` — 消融「一次只改一个因子」、实验矩阵、资源估算、分析计划先于开做。把 GPU hours 改成：**设备小时 + 样品数 + 外送排队**。

无这些文件或无 Python：**不要等脚本。** 就地交付：主张与证伪句、对照、独立重复单元、因子水平表（≤2 因子单扫；≥3 先筛 2–4 个再精）、每项表征对应哪句主张。标明「未跑 pyDOE」。禁止编造最优参数或检测限。Fisher：随机化、在处理施加的层级重复、区组批次/日期。伪重复：n=独立样品/器件/炉次，不是同一片的 20 张 SEM。

## 导师叠加

### 先主张后手段

「若假设为真，在 ____ 条件下将看到 ____；若假，将看到 ____。」没有这句，不准排表征菜单。

### 工科单元（防伪重复）

- 处理加在**样品/器件/批次**上，则 n = 独立样品数，不是同一片拍的 20 张 SEM。
- 同一炉、同一片晶圆上的多点，默认不是独立重复，除非论证。
- 报告均值与分散，禁止用冠军样品当规律。

### 表征为主张服务

每项 SEM/XRD/XPS/IV/阻抗/DSC… 填：支持哪句主张、样品态、量程够不够、排队。砍「别人都有所以我也拍」。

仿真：控制方程、边界、网格无关、用哪组实验校准哪几个参数；未校准标为趋势工具。

### 预实验时间盒

2–4 周只回答：做得出来吗、噪声是否吞掉效应、基线能否复现。失败是信息。

### 安全

无 SOP 的高温高压、强腐蚀、激光、高电压、纳米粉尘：**停止细化操作参数**，只给培训路径。不编仪器检测限。

## 输出

主张与证伪 | 独立重复单元 | 对照 | 因子水平或 DOE 表（优先用上游脚本） | 表征-主张表 | 仿真校准 | 统计 | 设备日程 | 失败备路。

REGISTRY id：sci.experimental-design · sci.statistical-power · phd.experiment-design
