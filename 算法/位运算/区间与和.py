# 返回区间[left right]内所有数&的结果

def rangeBitwiseAnd(left: int, right: int) -> int:
    while left < right:
        # 将right的二进制最后一个1变成0
        right = right & (right - 1)
    return right  

print(rangeBitwiseAnd(5, 7))
