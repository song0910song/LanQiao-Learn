# 2.棒球比赛

from typing import List

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score = []

        for i in operations:
            if '0' <= i[-1] <= '9':
                score.append(int(i))
            elif i == 'C':
                score.pop()
            elif i == 'D':
                score.append(score[-1] * 2)
            elif i == '+':
                score.append(score[-1] + score[-2])

        return sum(score)
    

t = Solution().calPoints(["1"])
print(t)