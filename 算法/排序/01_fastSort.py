# 快速排序 - 归并排序

def Sort(arr):
    if (len(arr) <= 1):
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = Sort(arr[:mid]) # 左边
    right = Sort(arr[mid:]) # 右边

    return merge(left, right)

def merge(left, right):
    helpArr = []

    l,r = 0, 0
    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            helpArr.append(left[l])
            l += 1
        else:
            helpArr.append(right[r])
            r += 1
    helpArr.extend(left[l:])
    helpArr.extend(right[r:])

    return helpArr

n = int(input())
nums = list(map(int, input().split()))

print(*Sort(nums))