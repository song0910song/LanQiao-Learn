# 多项式

from random import randint

# n = int(input())
# nums = list(map(int, input().split()))


def test(n, nums):
    s = ""

    isStart = 1

    for i in range(n - 1, -1, -1):
        t = n - 1 - i

        if nums[t] != 0:
            if nums[t] > 0:
                if nums[t] == 1:
                    s += f"{'' if isStart else '+'}x{f'^{i+1}' if t != n-1 else ''}"
                    isStart = 0
                else:
                    s += f"{'' if isStart else '+'}{nums[t]}x{f'^{i+1}' if t != n-1 else ''}"
                    isStart = 0
            else:
                if nums[t] == -1:
                    s += f"-x{f'^{i+1}' if t != n-1 else ''}"
                    isStart = 0
                else:
                    s += f"{nums[t]}x{f'^{i+1}' if t != n-1 else ''}"
                    isStart = 0

    if nums[-1] != 0:
        if isStart:
            s = f"{nums[-1]}"
        else:
            s += f"{'+' if nums[-1] > 0 else ''}{nums[-1]}"

    print(s)


for i in range(20):
    n = randint(0, 100)
    nums = [randint(-100, 100) for j in range(n + 1)]
    print(f"n: {n}")
    test(n, nums)
    print("\n\n")
