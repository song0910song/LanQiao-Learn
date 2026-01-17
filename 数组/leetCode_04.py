
# 1365. 有多少小于当前数字的数字

# from typing import List

# class Solution:
#     def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
#         smallerNumCount = []
#         lenNum = len(nums)

#         for i in range(lenNum):
#             count = 0
#             for j in nums:
#                 if nums[i] > j:
#                     count += 1

#             smallerNumCount.append(count)

from typing import List

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        # 对数组进行排序
        sorted_nums = sorted(nums)
        # 创建字典记录每个数字第一次出现的位置（即比它小的数字个数）
        count_dict = {}
        for i, num in enumerate(sorted_nums):
            if num not in count_dict:
                count_dict[num] = i
                print(count_dict)
        # 根据原始数组构建结果
        print(count_dict)
        return [count_dict[num] for num in nums]

s = Solution()
print(s.smallerNumbersThanCurrent([8,1,2,2,3]))