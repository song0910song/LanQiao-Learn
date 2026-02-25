import math

def f(arr: list[int], p: int):
    mod = sum(arr) % p

    if mod == 0:
        return 0
    
    sum_map = {0: -1}
    ans = math.inf
    find = 0
    cur = 0

    for i in range(len(arr)):
        # 0...i这部分的余数
        cur = (cur + arr[i]) % p
        find = cur - mod if cur >= mod else cur - mod + p

        # 如果之前出现过find这个余数，说明0...sum_map[find]这部分的余数是find，那么sum_map[find]+1...i这部分的余数就是mod
        if find in sum_map:
            ans = min(ans, i - sum_map[find])
        sum_map[cur] = i
    
    return ans if ans != len(arr) else -1

t = [3, 1, 4, 2]
p = 6
print(f(t, p))
