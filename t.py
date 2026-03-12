from typing import List
from math import inf
from collections import defaultdict
from bisect import bisect_right, bisect_left
from collections import defaultdict

class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)

        # key: nums的元素；values：nums的元素的下标
        indices = defaultdict(list)
        for i, num in enumerate(nums):
            indices[num].append(i)

        for key, value in indices.items():
            start = value[0]
            end = value[-1]
            indices[key].insert(0, end - n)
            indices[key].append(start + n)
        
        ans = []

        for i in queries:
            if len(indices[nums[i]]) == 3:
                ans.append(-1)
                continue
            j = bisect_left(indices[nums[i]], i)
            distance = min(i - indices[nums[i]][j-1], indices[nums[i]][j+1] - i)
            ans.append(distance)

        return ans



        
s = Solution()
print(s.solveQueries([1,3,1,4,1,3,2], [0,3,5]))