# SPDX-License-Identifier: Apache-2.0
# Copyright 2026 chenhz01 (EIM-1.0)
"""P46 consensus-fork-detector — 多智能体验证 oracle

L0: 大家意见分裂成几派时，这个工具把派别分出来。
L1: 按答案分组即派别。
L2: fork(opinions) → {answer: [agents]}。
"""

def fork(opinions):
    out = {}
    for agent, ans in opinions.items(): out.setdefault(ans, []).append(agent)
    return out

def demo():
    print("[P46]", fork({"a":"yes","b":"no","c":"yes"}))


if __name__ == "__main__":
    demo()
