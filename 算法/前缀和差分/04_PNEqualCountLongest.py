# 正负一样长的最长子数组

def getMaxLength(nums):

    sum_arr = 0
    # key: 前缀和
    # value: 前缀和最早出现的位置
    sum_map = {0: -1}
    # 答案
    ans = 0

    for i in range(len(nums)):
        sum_arr += nums[i]
        # print(sum_arr)
        # 如果前缀和之前出现过，说明之前的前缀和到现在的前缀和之间的子数组的累加和为0
        if sum_map.get(sum_arr) is not None:
            ans = max(ans, i - sum_map[sum_arr])
        else:
            sum_map[sum_arr] = i
    return ans

def getMaxLength2(nums):
    ans = 0

    for i in range(len(nums)):
        for j in range(i, len(nums)):
            sum_arr = 0
            for k in range(i, j+1):
                sum_arr += nums[k]
            if sum_arr == 0:
                ans = max(ans, j - i + 1)
    return ans
            


from random import randint

def validate():
    for _ in range(1000):
        arr = [randint(-1, 1) for _ in range(randint(1, 20))]
        if getMaxLength(arr) != getMaxLength2(arr):
            print("Oops!")
            print(arr)
            print(getMaxLength(arr))
            print(getMaxLength2(arr))
            break
    else:
        print("Nice!")

validate()