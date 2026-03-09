from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        path = []

        # 回溯函数
        def backtracking(start):

            # 终止条件
            if len(path) == k:
                res.append(path[:])
                return
            
            # 剪枝：当剩余的数字不足以填满 path 时，直接返回
            for i in range(start, n - (k - len(path)) + 2):
                path.append(i)
                backtracking(i + 1) # 递归
                path.pop() # 回退
        
        backtracking(1)
        return res