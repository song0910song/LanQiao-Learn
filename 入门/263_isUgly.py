from typing import List
from random import randint

class Solution:
    def isUgly(self, n: int) -> bool:

        # n要大于0
        if n <= 0:
            return False

        num = 0 # 标记[2, 3, 5]中的数
        while n > 1:
            if (n % 2 == 0):
                num = 2
            elif (n % 3 == 0):
                num = 3
            elif (n % 5 == 0):
                num = 5
            else:
                return False
            
            n //= num

        return True




tests = [randint(1, 100) for i in range(randint(1, 100))]

for test in tests:
    t = Solution().isUgly(test)
    print(f"{test}: {t}")

# t = Solution().isUgly(100)
# print(t)