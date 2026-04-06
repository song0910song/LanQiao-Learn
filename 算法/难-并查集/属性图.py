# https://leetcode.cn/problems/properties-graph/solutions/3624345/bing-cha-ji-pythonjavacgo-by-endlesschen-xi0d/
from typing import List

class Solution:
    def numberOfComponents(self, properties: List[List[int]], k: int) -> int:
        properties_1 = [set(propertie) for propertie in properties]
        # print(properties_1)
        n = len(properties_1)
        father = list(range(n))
        
        for i in range(n):
            for j in range(i+1, n):
                a, b = properties_1[i], properties_1[j]
                diff_num = len(a & b)
                if diff_num >= k:
                    self.union(father, i, j)
        # print(father)
        return len(set([self.find(father, i) for i in range(n)]))
            

    def find(self, arr, x):
        if arr[x] != x:
            arr[x] = self.find(arr, arr[x])
        return arr[x]
    
    def union(self, arr, a, b):
        a, b = self.find(arr, a), self.find(arr, b)
        if (a != b):
            arr[b] = a

# a = set([1,1])
# b = set([2,3])
# print((a | b) - (a & b))

t = Solution()
print(t.numberOfComponents([[1,2,3],[2,3,4],[4,3,5]], 2))