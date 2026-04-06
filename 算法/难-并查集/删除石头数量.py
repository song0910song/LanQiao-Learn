# 题目：947. 移除最多的同行或同列石头
# https://leetcode.cn/problems/most-stones-removed-with-same-row-or-column/



from typing import List

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        father = [i for i in range(n)]

        firstCow = {}
        firstLine = {}

        for i, num in enumerate(stones):
            cow, line = num[0], num[1]
            if firstCow.get(cow) is not None:
                self.union(i, firstCow[cow], father)
            else:
                firstCow[cow] = i
            if firstLine.get(line) is not None:
                self.union(i, firstLine[line], father)
            else:
                firstLine[line] = i

        # print(father)
        return n - len(set([self.find(i, father) for i in range(n)]))

    def find(self, x, arr):
        if arr[x] != x:
            arr[x] = self.find(arr[x], arr)
        return arr[x]
    
    def union(self, a, b, arr):
        x, y = self.find(a, arr), self.find(b, arr)
        arr[y] = x

t = Solution()
print(t.removeStones([[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]))
