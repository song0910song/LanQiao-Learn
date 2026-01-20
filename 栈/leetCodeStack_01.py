# LeetCode 用栈操作构建数组

from typing import List

class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:

        text = [] # 输出操作
        stack = [] # 栈操作

        for i in range(1, n+1):
            if stack == target:
                break
            text.append('Push')
            stack.append(i)
            if i not in target:
                text.append('Pop')
                stack.pop()

        return text