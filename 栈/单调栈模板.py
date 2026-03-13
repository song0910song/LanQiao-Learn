# 单调栈模板

import sys

def solve() -> None:
    data = iter(map(int, sys.stdin.read().split()))
    n = next(data)
    arr = [next(data) for _ in range(n)]

    stack = []
    # ans[i][0]表示左边第一个比arr[i]小的数的索引，ans[i][1]表示右边第一个比arr[i]小的数的索引
    ans = [[-1 for _ in range(2)] for _ in range(n)]
    for i in range(n):
        # 维护一个单调递增的栈，栈顶元素对应的值最小
        while stack and arr[stack[-1]] >= arr[i]:
            cur = stack.pop()
            ans[cur][1] = i
            ans[cur][0] = stack[-1] if stack else -1
        stack.append(i)

    # 处理剩余的元素
    while stack:
        cur = stack.pop()
        ans[cur][1] = -1
        ans[cur][0] = stack[-1] if stack else -1

    # 处理重复元素
    for i in range(n-2, -1, -1):
        if ans[i][1] != -1 and arr[ans[i][1]] == arr[i]:
            ans[i][1] = ans[ans[i][1]][1]

    print(ans)
    print(stack)


solve()