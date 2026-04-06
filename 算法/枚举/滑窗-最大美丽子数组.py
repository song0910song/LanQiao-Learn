# 题目：https://leetcode.cn/problems/maximum-beauty-of-an-array-after-applying-operation/solutions/2345805/pai-xu-shuang-zhi-zhen-by-endlesscheng-hbqx/
# 思路：排序 + 不定长滑窗

from typing import List
class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)

        left = max_len = 0
        for i, num in enumerate(nums):
            
            while num - nums[left] > 2 * k:
                left += 1

            max_len = max(max_len, i - left + 1)
            
        return max_len
    

