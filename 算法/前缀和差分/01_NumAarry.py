# 子数组求和问题

def NumArray(arr: list[int]) -> list[int]:
    sum_arr = [0] * (len(arr) + 1)
    for i in range(1, len(arr) + 1):
        sum_arr[i] = sum_arr[i - 1] + arr[i - 1]
    return sum_arr

def sum_range(sum_arr: list[int], i: int, j: int) -> int:
    return sum_arr[j+1] - sum_arr[i]

t = [3, 2, -5, 6, 2, 1]
print(NumArray(t))
print(sum_range(NumArray(t), 2, 3))
