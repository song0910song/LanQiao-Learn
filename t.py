def solve_one(arr):
    vis = [False] * 9
    for x in arr:
        vis[x] = True

    pos = [i for i in range(1, 9) if vis[i]]
    k = len(pos)
    if k <= 1:
        return 0

    max_gap = 0
    for i in range(k - 1):
        max_gap = max(max_gap, pos[i + 1] - pos[i])
    max_gap = max(max_gap, pos[0] + 8 - pos[-1])

    return 8 - max_gap