# 可以拆分为：
#1.老板不生气的顾客数量p1
#2.在minutes时间内老板生气的顾客数量最大值maxP1
#3.最终答案为：p1 + maxP1

from typing import List
class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        s = [0, 0]
        maxP1 = 0

        for i, (c, g) in enumerate(zip(customers, grumpy)):
            s[g] += c
            left = i - minutes + 1
            if left < 0:
                continue

            # 更新生气时顾客数量的最大值
            maxP1 = max(maxP1, s[1])

            if grumpy[left]:
                s[1] -= customers[left]
            
        return s[0] + maxP1

t = Solution()
print(t.maxSatisfied([7, 8, 8, 6], [0, 1, 0, 1], 3))