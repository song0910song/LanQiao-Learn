# 求最大值

def find_maximum(arr:list[int]) -> int:
    if len(arr) == 1:
        return arr[0]
    
    mid = len(arr) // 2
    left_max = find_maximum(arr[:mid])
    right_max = find_maximum(arr[mid:])
    return max(left_max, right_max)
    

arr = [3, 1, 4, 1, 5, 9, 2, 6, 5]
print(find_maximum(arr))