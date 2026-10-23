# SPDX-License-Identifier: Apache-2.0
# Copyright 2026 chenhz01 (EIM-1.0)
"""P44 agent-output-verifier — 多智能体验证 oracle

L0: 几个 AI 各给一个答案，交叉比对，找出那个不对劲的。
L1: 多数投票得共识，偏离共识者为 outlier。
L2: verify(outputs) → (consensus, outliers)。
"""

def verify(outputs):
    from collections import Counter
    if not outputs: return (None, [])
    cand, n = Counter(outputs).most_common(1)[0]
    out = [o for o in outputs if o != cand]
    return cand, out

def demo():
    print("[P44]", verify(["42","42","41","42"]))


if __name__ == "__main__":
    demo()
