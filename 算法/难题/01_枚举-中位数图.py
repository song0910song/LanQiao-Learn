# 题目链接："https://ac.nowcoder.com/acm/contest/20960/1011"
# 题目描述：

import sys
# 思路：
# 1. 首先将数组中的元素根据与b的关系转换为-1、0、1，记录b的位置。
# 2. 从b的位置向右遍历，计算平衡值（-1和1的累计和），并记录每个平衡值出现的次数。
# 3. 从b的位置向左遍历，计算平衡值，并根据右侧记录的平衡值次数来统计满足条件的子数组数量。

def solution(arr, n, b):
    pos = -1
    transformed = [0] * n
    for i, value in enumerate(arr):
        if value < b:
            transformed[i] = -1
        elif value > b:
            transformed[i] = 1
        else:
            transformed[i] = 0
            pos = i

    if pos == -1:
        return 0

    right_count = {}
    balance = 0
    for i in range(pos, n):
        balance += transformed[i]
        right_count[balance] = right_count.get(balance, 0) + 1

    ans = 0
    balance = 0
    for i in range(pos, -1, -1):
        balance += transformed[i]
        ans += right_count.get(-balance, 0)

    return ans


def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    n = int(data[0])
    b = int(data[1])
    arr = list(map(int, data[2:2 + n]))
    print(solution(arr, n, b))


if __name__ == "__main__":
    main()
