# P46 · consensus-fork-detector

> 机制簇：**多智能体验证 oracle** ｜ 家族：**EIM-1.0**（55 个涌现智能人工化机制之一）

## 费曼三层

**L0 · 这是什么（12 岁能懂）**
大家意见分裂成几派时，这个工具把派别分出来。

**L1 · 机制本质**
按答案分组即派别。

**L2 · 怎么用上**
fork(opinions) → {answer: [agents]}。

## 30 秒跑起来

```bash
python impl.py        # 看 demo 输出
python selftest.py    # 跑自检（含输出快照比对）
```

真实运行输出（本仓发布时快照，`golden_output.txt` 同内容）：

```text
[P46] {'yes': ['a', 'c'], 'no': ['b']}
```

## 什么时候该用 / 不该用

| | 内容 |
|---|---|
| **该用** | 高价值、不可逆决策；单模型置信度不足、需要交叉验证的场合。 |
| **不该用** | 低风险高频调用；延迟敏感的实时链路。 |
| **常见误用** | 用同源模型的多实例冒充独立验证——共同盲区不会因为多开几个而消失。 |

## 在这个家族里

- 组合仓（55 个机制合集）：https://github.com/chenhz01/emergent-mechanisms
- 同簇伙伴：`P44` agent-output-verifier · `P45` oracle-compiler-bridge · `P47` role-isolation-tester
- 本仓是 **P46 的独立署名锚**：可单独引用、单独开 issue、单独打星；实现与组合仓
  `components/P46-consensus-fork-detector/` 一致，修复会双向同步。

## License

**双许可**：

- **代码**：Apache-2.0 — 见 [LICENSE](LICENSE)
- **文档/规范**：CC BY 4.0 — 见 [LICENSE-SPEC](LICENSE-SPEC)

对外声明「符合 / 兼容 / 通过 EIM-1.0」时须署名：
`EIM-1.0 · P46 · consensus-fork-detector © 2026 chenhz01, CC BY 4.0`
未作上述声明者可自由使用、商用、闭源、改名，无需署名。详见 [NOTICE](NOTICE)。
