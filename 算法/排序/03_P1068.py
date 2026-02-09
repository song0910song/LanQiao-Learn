# 分数线

import math
import functools

n, m = map(int, input().split())

d = {}
for i in range(n):
    num, score = map(int, input().split())
    d[num] = score


d = sorted(d.items(), key=lambda x: (-x[1], x[0]))

pass_n = math.floor(m * 1.5) - 1
last = d[pass_n][1]
for i in range(pass_n+1, len(d)):
    if last == d[i][1]:
        pass_n += 1

print(f"{d[pass_n][1]} {pass_n+1}")
for i in range(pass_n+1):
    print(f"{d[i][0]} {d[i][1]}")