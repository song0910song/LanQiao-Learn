from typing import List
from math import inf
from collections import defaultdict
from bisect import bisect_right, bisect_left

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        p = sorted(potions)
        n = len(p)
        print(p)

        return [n - bisect_left(p, success // si + 1) for si in spells]


s = Solution()
print(s.successfulPairs([3,1,2], [8, 5, 8], 16))
import math
print(math.ceil(16 / 3))