# # 逆序对
import sys

# ans = 0
# n = int(input())
# t = sys.stdin.read()
# t = list(map(int, t.strip('\n').split()))
# helpArr = [0] * n


# # 归并排序
# def Sort(l, r):
#     # 基线条件
#     if l == r:
#         return 0

#     # 递归条件
#     mid = (l + r) // 2

#     Sort(l, mid)
#     Sort(mid + 1, r)

#     return Sort(l, mid) + Sort(mid+1 , r) + merge(l, mid, r)


# def merge(l, mid, r):
#     global ans
#     k, i, j = l, l, mid + 1
#     # 排序、合并
#     while i <= mid and j <= r:
#         if t[i] <= t[j]:
#             helpArr[k] = t[i]
#             i += 1
#         else:
#             helpArr[k] = t[j]
#             j += 1
#             ans += mid - i + 1
#         k += 1

#     while i <= mid:
#         helpArr[k] = t[i]
#         i += 1
#         k += 1

#     while j <= r:
#         helpArr[k] = t[j]
#         j += 1
#         k += 1

#     # 将排序好的数组复制回原数组
#     for k in range(l, r + 1):
#         t[k] = helpArr[k]

#     return ans



# Sort(0, n - 1)
# print(ans)

def count_inversions_compact(arr):
    """
    简洁版的归并排序逆序对统计
    """
    if len(arr) <= 1:
        return arr, 0
    
    mid = len(arr) // 2
    left, count_left = count_inversions_compact(arr[:mid])
    right, count_right = count_inversions_compact(arr[mid:])
    
    merged = []
    i = j = 0
    inversions = count_left + count_right
    len_left, len_right = len(left), len(right)
    
    while i < len_left and j < len_right:
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            inversions += len_left - i  # 关键统计步骤
            j += 1
    
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged, inversions

def count_inversions(arr):
    """
    简洁版入口函数
    """
    _, count = count_inversions_compact(arr)
    return count

# 测试示例
n = int(input())
t = sys.stdin.read()
t = list(map(int, t.strip('\n').split()))
print(count_inversions(t))