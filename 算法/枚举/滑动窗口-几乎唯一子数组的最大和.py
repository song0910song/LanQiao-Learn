# 题目："https://leetcode.cn/problems/maximum-sum-of-almost-unique-subarray/"
'''
解题思路：
1. 使用定长滑动窗口，窗口大小为 k
2. 维护一个哈希表记录窗口内元素的频次
3. 维护窗口内元素的和: 当窗口右边界移动时，加入新元素的值；当窗口左边界移动时，减去移出元素的值
4. 当窗口内唯一元素的个数满足条件时，更新最大和
'''

from collections import defaultdict
from typing import List

class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        arr_sum = 0
        max_sum = 0

        # 记录重复值
        # key: 数组值
        # value: 出现的次数
        repeat = defaultdict(int)

        for i, num in enumerate(nums):
            # 进入窗口
            arr_sum += num
            repeat[num] += 1

            left = i - k + 1
            if left < 0:
                continue
            
            # 更新元素和的最大值
            if len(repeat) >= m:
                max_sum = max(max_sum, arr_sum)
            
            # 离开窗口
            out = nums[left]
            repeat[out] -= 1
            # 如果元素的频次为0，说明该元素不再窗口内，删除该元素的记录
            if repeat[out] == 0:
                del repeat[out]
            arr_sum -= out

        return max_sum
