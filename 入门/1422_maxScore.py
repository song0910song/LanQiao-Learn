# 1422 分割字符串的最大得分

class Solution:
    def maxScore(self,s: str) -> int:
        left = 0 # 左边
        right = len(s) # 右边
        maxNum = 0

        for i in range(1, len(s)):
            leftzeros = s[0:i].count('0')
            rightOnes = s[i:].count('1')

            maxNum = max(maxNum, leftzeros+rightOnes)
        
        return maxNum
            
# print('sdsds'[0:1])
