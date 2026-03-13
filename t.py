from typing import List
from itertools import accumulate
from math import inf
# print(list(accumulate([1,-3,2,3,-4], initial=0)))

def findLockNum(nums: List[int]) -> int:
    eorAll = eorHas = 0

    for i in range(len(nums)):
        eorAll ^= i
        eorHas ^= nums[i]
    
    eorAll ^= len(nums)
    return eorAll ^ eorHas

print(findLockNum([3, 0, 1]))