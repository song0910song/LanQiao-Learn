# 题目：https://ac.nowcoder.com/acm/contest/125955/D
# 考点：集合的并集、前缀和、差分

import sys


def add_range(diff, l, r):
    if l > r:
        return
    diff[l] += 1
    diff[r + 1] -= 1


def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    t = data[0]
    idx = 1
    out_lines = []

    for _ in range(t):
        n, q = data[idx], data[idx + 1]
        idx += 2

        diff = [0] * (n + 3)

        for _ in range(n):
            ai, bi = data[idx], data[idx + 1]
            idx += 2

            # 计算 ai 和 bi 的邻近位置，形成两个区间 [l1, r1] 和 [l2, r2]
            l1 = max(1, ai - 1)
            r1 = min(n, ai + 1)
            l2 = max(1, bi - 1)
            r2 = min(n, bi + 1)

            # 计算两个区间 [l1, r1] 和 [l2, r2] 的并集，并在 diff 中标记这个并集的范围
            if l2 <= r1 + 1:
                add_range(diff, l1, max(r1, r2))
            else:
                add_range(diff, l1, r1)
                add_range(diff, l2, r2)

        good = [0] * (n + 1)
        cur = 0
        for x in range(1, n + 1):
            cur += diff[x]
            good[x] = cur

        ans = []
        for _ in range(q):
            x = data[idx]
            idx += 1
            ans.append(str(n - good[x]))

        out_lines.append(" ".join(ans))

    sys.stdout.write("\n".join(out_lines))


if __name__ == "__main__":
    solve()
    