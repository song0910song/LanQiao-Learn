from typing import List
from math import inf

class Solution:
    def maxScore_1(self, cardPoints: List[int], k: int) -> int:
        # 逆向思维：剩下的n-k是连续数组，要使点数最大，则剩下的点数最小
        new_k = len(cardPoints) - k
        min_arr = inf
        s = 0

        if new_k == 0:
            return sum(cardPoints)

        for i, num in enumerate(cardPoints):
            s += num
            left = i - new_k + 1
            if left < 0:
                continue 
            
            min_arr = min(s, min_arr)

            s -= cardPoints[left]

        return int(sum(cardPoints) - min_arr)
    

    def maxScore_2(self, cardPoints: List[int], k: int) -> int:
        # 正向思维
        '''
        1. 前k个元素和
        2. 前k-1个元素和 + 最后一个元素
        3. 前k-2个元素和 + 最后两个元素
        ...
        k. 最后k个元素和
        '''

        ans = s = sum(cardPoints[:k])

        for i in range(1, k+1):
            s += cardPoints[-i] - cardPoints[k - i]
            ans = max(ans, s)

        return ans