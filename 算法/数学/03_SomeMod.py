# 同余原理举例

from random import randint


# 计算 ((a + b) * (c - d) + (a * c - b * d)) % mod的结果
def f1(a, b, c, d, mod):
    total = ((a + b) * (c - d) + (a * c - b * d)) % mod
    return int(total) if total >= 0 else int(total + mod)


def f2(a, b, c, d, mod):
    o1 = a % mod  # o1
    o2 = b % mod  # o2
    o3 = c % mod  # o3
    o4 = d % mod  # o4
    o5 = (o1 + o2) % mod  # (a + b)
    o6 = (o3 - o4 + mod) % mod  # (c - d)
    o7 = (o1 * o3) % mod  # (a * c)
    o8 = (o2 * o4) % mod  # (b * d)
    o9 = (o5 * o6) % mod  # (a + b) * (c - d)
    o10 = (o7 - o8 + mod) % mod  # (a * c - b * d) % mod
    ans = (o9 + o10) % mod

    return ans


def random():
    return randint(10**6, 10**8)


a = random()
b = random()
c = random()
d = random()
MOD = 10**8 + 7

print("测试开始")
print("=" * 20)
print(f"a={a}\nb={b}\nc={c}\nd={d}")
print()
print(f1(a, b, c, d, MOD))
print(f2(a, b, c, d, MOD))
