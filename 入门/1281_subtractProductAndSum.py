# 1281. 整数的各位积和之差

from random import randint

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        add = 0 # 各个位数相加
        product = 1 # 各个位数相乘

        while n > 0:
        	signle = n % 10
        	add += signle
        	product *= signle
        	n //= 10

        return product - add

test = randint(1, pow(10, 5)) # 随机整数

print(test)
print(Solution().subtractProductAndSum(test))