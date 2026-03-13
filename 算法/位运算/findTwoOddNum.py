# 找到2种出现奇数次的数

def find_odd_num(nums):
    eor = 0

    # eor的结果是a^b
    for num in nums:
        eor ^= num
    
    # brian Kernighan算法，找到eor最右侧的1
    rightOne = eor & (-eor)
    onlyOne = 0

    # 根据rightOne将nums分成两类，找到其中一类的a或b
    for num in nums:
        if (num & rightOne) == 0:
            onlyOne ^= num
    
    return [onlyOne, onlyOne ^ eor]

print(find_odd_num([1, 2, 3, 2, 3, 1, 3, 4]))