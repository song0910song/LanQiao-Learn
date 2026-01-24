from typing import List, Optional
from collections import Counter


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        lenNums = len(nums)

        # 方法一：暴力破解
        for i in range(lenNums):
            for j in range(i + 1, lenNums):
                if nums[j] == nums[i]:
                    count += 1

        # 方法二：组合计数
        m = Counter(nums)  # 统计各个数字出现的次数
        count2 = sum(v * (v - 1) // 2 for k, v in m.items())

        return [count2, count]


t = Solution().numIdenticalPairs([1, 2, 3, 1, 1, 3])
print(t)
