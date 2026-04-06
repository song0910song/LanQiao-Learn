# 题目：https://ac.nowcoder.com/acm/contest/125955/C
# 考察点：思维题，模拟题，数学题

import sys
import math

t = int(input())

ans = []
for i in range(t):
    cnt = {}
    sum_num = 0
    n, p, k = map(int, input().split())
    
    for j in range(n):
        s, a = input().split()
        cnt[s] = int(a)
        sum_num += int(a)
        
    mn = math.inf
    
    for j in range(k):
        t_i = input()
        mn = min(mn, cnt[t_i])
        
    if mn * p < sum_num:
        ans.append('-1')
    else:
        ans.append(f'{sum_num // p + 1} {mn}')
    
sys.stdout.write('\n'.join(ans))

# 向上取整
print(math.ceil(6))