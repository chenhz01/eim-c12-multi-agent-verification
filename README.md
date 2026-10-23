# C12 · Multi-Agent Verification

> **机制簇**：多智能体验证 oracle ｜ **家族**：EIM-1.0（Emergent Intelligence Mechanisms）｜ **组件数**：4
>
> 本仓是 EIM-1.0 的**簇级入口**：一个机制簇 + 该簇全部可运行参考实现。
> 单组件仓与旗舰合集见文末「家族」段。

## 费曼三层

**L0 · 这是什么（12 岁能懂）**
多个 AI 各做一遍再互相对答案，对不上的地方就是可疑处，专门去查。

**L1 · 机制本质**
交叉验证 + 分歧定位 + 最小修复建议；接编译器/测试等确定性 oracle 兜底。

**L2 · 怎么用上**
cross-verifier 比对；disagreement-locator 定位分歧段；oracle-binder 接确定性验证。

## 30 秒跑起来

```bash
git clone https://github.com/chenhz01/eim-c12-multi-agent-verification.git && cd eim-c12-multi-agent-verification
python run_all.py        # 跑全簇 4 个组件，逐个 selftest + 输出快照比对
```

单个组件也可独立跑：

```bash
python components/p44-agent-output-verifier/impl.py        # 看 demo 输出
python components/p44-agent-output-verifier/selftest.py    # 断言 + 与 golden_output.txt 比对
```

零第三方依赖，Python 3.9+ 即可。

## 本簇组件

| ID | 组件 | 机制本质 | 目录 |
|---|---|---|---|
| `P44` | agent-output-verifier | 多数投票得共识，偏离共识者为 outlier。 | `components/p44-agent-output-verifier/` |
| `P45` | oracle-compiler-bridge | 调用外部 oracle_fn 校验，返回 pass/fail + 原因。 | `components/p45-oracle-compiler-bridge/` |
| `P46` | consensus-fork-detector | 按答案分组即派别。 | `components/p46-consensus-fork-detector/` |
| `P47` | role-isolation-tester | 比对两 agent 状态键交集，非空即泄漏。 | `components/p47-role-isolation-tester/` |

## 该用 / 不该用 / 常见误用

**该用**
高风险产出（涉及钱、权限、数据迁移）需要第二意见的场景。

**不该用**
主观创作（无客观对错）；成本极敏感的低价值任务。

**常见误用（这条最重要）**
把多数票当真理。同源模型会一起错——必须异源 + 确定性 oracle 才有意义。

## 这份代码是什么、不是什么

- **是**：可直接运行、带断言与输出快照的最小参考实现。每个 `impl.py` 都能单独跑出 demo，`selftest.py` 会在行为漂移时报错。
- **不是**：生产级库。缺少配置化、并发安全、错误恢复、性能优化。**生产使用请按自己的约束扩展**，不要原样上生产。
- **诚实边界**：本簇解决的是「机制怎么落地」这个问题，不承诺在任何数据分布下都优于基线。基准数据请自测。

## 家族

- **旗舰合集（55 组件）**：https://github.com/chenhz01/emergent-mechanisms
- **单组件仓**：`eim-p01-…` ~ `eim-p55-…`，与 `components/` 内文件一致，任一处修复会双向同步。

## 许可（双许可）

- **代码**：**Apache-2.0**（Apache License 2.0）— 见 [LICENSE](LICENSE)
- **规范/文档**：**CC BY 4.0**（Creative Commons Attribution 4.0 International）— 见 [LICENSE-SPEC](LICENSE-SPEC)

声明符合 EIM-1.0 规范时须署名：

```
EIM-1.0 · C12 · Multi-Agent Verification © 2026 chenhz01, CC BY 4.0
```

详见 [NOTICE](NOTICE)。
