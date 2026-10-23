# SPDX-License-Identifier: Apache-2.0
# Copyright 2026 chenhz01 (EIM-1.0)
"""P47 role-isolation-tester — 多智能体验证 oracle

L0: 检查两个 AI 的'私密记忆'有没有互相串味。
L1: 比对两 agent 状态键交集，非空即泄漏。
L2: leaks(state_a, state_b) → 泄漏键。
"""

def leaks(a, b):
    return sorted(set(a) & set(b))

def demo():
    print("[P47]", leaks({"role","secret_x"}, {"role","task"}))


if __name__ == "__main__":
    demo()
