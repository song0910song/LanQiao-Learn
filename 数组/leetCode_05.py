# 找到所有数组中消失的数字

from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        numsDict = {}
        ans = []

        for num in nums:
        	numsDict[num] = numsDict.get(num, 0) + 1

        for i,num in enumerate(nums):
        	if numsDict.get(i+1, 0) == 0:
        		ans.append(i+1)

       	return ans


# 2. 哈希表原地修改数组