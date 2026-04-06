# 快速排序 - 归并排序

# 递归实现
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


# def Sort(arr):
#     n = len(arr)

#     temp = [0] * n
#     step = 1

#     while step < n:
#         left = 0

#         while left < n:
#             mid = min(left+step, n)
#             right = min(left+2*step, n)

#             if mid < right:
#                 i,j,k = left, mid, left
#                 temp[left:right] = arr[left:right]

#                 while i < mid and j < right:
#                     if temp[i] <= temp[j]:
#                         arr[k] = temp[i]
#                         i += 1
#                         k += 1
#                     else:
#                         arr[k] = temp[j]
#                         j += 1
#                         k += 1
                
#                 while i < mid:
#                     arr[k] = temp[i]
#                     i += 1
#                     k += 1
#                 while j < right:
#                     arr[k] = temp[j]
#                     j += 1
#                     k += 1
#             left += 2*step
        
#         step *= 2

#     return arr

# n = int(input())
# nums = list(map(int, input().split()))
from random import randint

test = [randint(1, 100) for i in range(10)]
print(test)
print(Sort(test))

# print(*Sort(nums))
