# # 归并排序

# def Sort(arr, l, r):

#     # 递归停止条件
#     if (l == r):
#         return
    
#     # 递归部分
#     mid = (l + r) // 2
#     Sort(arr, l, mid)
#     Sort(arr, mid+1, r)

    
#     if l == 0 and r == len(arr) - 1:
#         return merge(arr, l, r, mid)
#     if (len(arr) > 1 and arr[mid] > arr[mid+1] ):
#         arr[l:r+1] = arr[mid+1:r+1] + arr[l:mid+1]

# def merge(arr, l, r, mid):
#     helpArr = []

#     i = mid + 1

#     if not arr:
#         return []

#     while l <= mid and i <= r:
#         if arr[l] > arr[i]:
#             helpArr.append(arr[i])
#             i += 1
#         else:
#             helpArr.append(arr[l])
#             l += 1
    
#     if l > mid:
#         helpArr.extend(arr[i:])
#     else:
#         helpArr.extend(arr[l: mid+1])

#     return helpArr
        
def merge_sort_recursive(arr):
    """
    递归实现归并排序
    
    参数:
    arr: 待排序的列表
    
    返回:
    排序后的列表
    """
    if len(arr) <= 1:
        return arr
    
    # 分割数组
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    # 递归排序左右子数组
    left_half = merge_sort_recursive(left_half)
    right_half = merge_sort_recursive(right_half)
    
    # 合并排序后的子数组
    return merge(left_half, right_half)

def merge(left, right):
    """
    合并两个已排序的数组
    
    参数:
    left: 左侧已排序数组
    right: 右侧已排序数组
    
    返回:
    合并后的排序数组
    """
    result = []
    i = j = 0
    
    # 比较两个数组的元素，依次放入结果数组
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # 添加剩余元素
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result

from random import randint

s = [randint(1, 100) for i in range(5)]

merge_sort_recursive(s)