'''
链接：https://ac.nowcoder.com/acm/contest/130832/A
来源：牛客网

tb 给了 fc 一个长度为𝑛的数组𝐴, fc对A进行k次如下操作：
删除数组第一个元素或者删除数组最后一个元素
求最后得到的数组和的最大值。
'''

import sys

n, k = map(int, input().split())
arr = list(map(int, sys.stdin.read().split()))

per_sum = [0] * (n+1)
for i in range(1, n+1):
    per_sum[i] = per_sum[i-1] + arr[i-1]

ans = 0
for i in range(k+1):
    s = per_sum[n - k + i] - per_sum[i]
    ans = max(ans, s)

print(ans)

r = set()
r.clear()
    
    
    
    