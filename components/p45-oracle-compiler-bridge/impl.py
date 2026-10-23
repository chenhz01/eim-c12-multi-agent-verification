# SPDX-License-Identifier: Apache-2.0
# Copyright 2026 chenhz01 (EIM-1.0)
"""P45 oracle-compiler-bridge — 多智能体验证 oracle

L0: 把 AI 的答案丢给编译器/检查器去判对错，不靠 AI 自评。
L1: 调用外部 oracle_fn 校验，返回 pass/fail + 原因。
L2: check(output, oracle_fn) → (bool, info)。
"""

def check(output, oracle_fn):
    try:
        ok = bool(oracle_fn(output))
        return ok, "ok" if ok else "rejected_by_oracle"
    except Exception as e:
        return False, f"oracle_error:{type(e).__name__}"

def demo():
    print("[P45]", check("1+1=2", lambda s: eval(s.split("=")[0]) == int(s.split("=")[1])))


if __name__ == "__main__":
    demo()
