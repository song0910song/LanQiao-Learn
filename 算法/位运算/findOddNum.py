# 找到出现奇数次的数

def find_odd_num(nums):
    eor = 0
    for num in nums:
        eor ^= num
    return eor

print(find_odd_num([1, 2, 3, 2, 3, 1, 3]))