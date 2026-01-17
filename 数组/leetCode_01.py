# LeetCode Array_01

from typing import List

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        arrayLen = len(nums)
        ans_arr = nums.copy()
        # for num in nums:
        #     ans_arr.append(num)
        ans_arr.extend(ans_arr)
        
        return ans_arr
    
# test = Solution()
# s = test.getConcatenation([1,2,3])
# print(s)
