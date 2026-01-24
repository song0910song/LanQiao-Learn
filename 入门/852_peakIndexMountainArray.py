# 852 山脉数组的峰顶索引

from typing import List

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left = 0
        right = len(arr)
        index = 0

        while left <= right:
            mid = (left + right) // 2
            if arr[mid] > arr[mid+1] and arr[mid] > arr[mid-1]:
                index = mid
                break
            elif arr[mid] > arr[mid-1] and arr[mid] < arr[mid+1]:
                left = mid
            elif arr[mid] < arr[mid-1] and arr[mid] > arr[mid+1]:
                right = mid
        return index
    
t = Solution().peakIndexInMountainArray([40,48,61,75,100,99,98,39,30,10])
print(t)