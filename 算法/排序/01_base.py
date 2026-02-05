# 基数排序
# 技巧：前缀和数量分区 + 数字提取每一位的技巧

t = [23, 11, 10, 123, 1]
# cnts = []
# arr = [0] * len(t)
# offest = 1
# bit = 3 # 最大数的位数

# for i in range(bit):
#     cnts = [0] * 10
#     for j in range(len(t)):
#         # 提取数字某一位的技巧
#         cnts[(t[j] // offest) % 10] += 1
#     # 前缀和累加
#     for j in range(1, 10):
#         cnts[j] = cnts[j] + cnts[j-1]
    
#     for j in range(len(t) - 1, -1 ,-1):
#         idx = cnts[(t[j] // offest) % 10]
#         arr[idx - 1] = t[j]
#         cnts[(t[j] // offest) % 10] -= 1
    
#     for j in range(len(t)):
#         t[j] = arr[j]

#     offest *= 10

def BaseSort(arr:list[int], bits:int, base:int = 10):
    '''
    :param arr: 待排序数组
    :type arr: list[int]
    :param bits: 数组中最大值的位数
    :type bits: int
    :param base: 进制数
    :type base: int
    '''

    offest = 1
    n = len(arr)
    helpArr = [0] *  n
    for i in range(bits):
        cnts = [0] * base  # 计数数组
        for j in range(n):
            # 提取某一位
            cnts[(t[j] // offest) % base] += 1
        
        # 前缀和分数量区间
        for j in range(1, base):
            cnts[j] = cnts[j] + cnts[j - 1]

        for j in range(n-1, -1, -1):
            idx = cnts[(t[j] // offest) % base]
            helpArr[idx - 1] = t[j]
            cnts[(t[j] // offest) % base] -= 1
        
        for j in range(n):
            arr[j] = helpArr[j]
        
        offest *= 10

BaseSort(t, 3, 10)
print(t)



