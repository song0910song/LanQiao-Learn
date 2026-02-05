# 分数线

import math
import functools

n, m = map(int, input().split())

d = {}
for i in range(n):
    num, score = map(int, input().split())
    d[num] = score


def cmp(a, b):
    if a[1] > b[1]:
        return -1
    elif a[1] < b[1]:
        return 1
    else:
        if a[0] > b[0]:
            return 1
        else:
            return -1

d = sorted(d.items(), key=functools.cmp_to_key(cmp))

pass_n = math.floor(m * 1.5) - 1
last = d[pass_n][1]
for i in range(pass_n+1, len(d)):
    if last == d[i][1]:
        pass_n += 1

print(f"{d[pass_n][1]} {pass_n+1}")
for i in range(pass_n+1):
    print(f"{d[i][0]} {d[i][1]}")