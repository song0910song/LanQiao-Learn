# 231 转置矩阵
from typing import List
from random import randint

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        row = len(matrix) 
        col = len(matrix[0])
        transMatrix = [[0] * row for _ in range(col)] # 转置行和列转换
        
        for i in range(col):
            for j in range(row):
                transMatrix[i][j] = matrix[j][i]

        return transMatrix

t = Solution().transpose([[1,2],[4,5],[7,8]])
print(t)