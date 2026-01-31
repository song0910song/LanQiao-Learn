# 分数线

import math

n, m = map(int, input().split())

d = {}
for i in range(n):
    num, score = map(int, input().split())
    d[num] = score

d = sorted(d.items(), key=lambda a:a[0], reverse=True)
pass_n = math.floor(m * 1.5)
if d[pass_n][1] == d[pass_n+1][1]:
    pass_n += 1

print(pass_n)