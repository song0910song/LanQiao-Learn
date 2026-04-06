# 题目：https://ac.nowcoder.com/acm/contest/123787/D

'''
方法：
x - a是x - b的倍数 --> (x - a) % (x - b) == 0
令 y = x - b，应为 b < x < r，所以 y > 0
(y + b - a) % y == 0 --> (b - a) % y == 0 --> y | (b - a)
'''

import sys
from math import sqrt
import bisect

s = [[] for _ in range(200000)]
for i in range(1, 200000):
    for j in range(i, 200000, i):
        s[j].append(i)

# print(s[2])  # [1, 2, 3, 4, 6, 12]

input = sys.stdin.readline
t = int(input())
ans = []
for _ in range(t):
    a, b, l, r = map(int, input().split())

    c = b - a
    
    # 计算 y 的范围
    li = l - b
    ri = r - b

    left = bisect.bisect_left(s[c], li)
    right = bisect.bisect_right(s[c], ri)
    ans.append(str(right - left))
print('\n'.join(ans))
