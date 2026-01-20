    # 258. 各位相加
from random import randint

class Solution1:
    def addDigits(self, num: int) -> int:

        # 1.循环
        numCopy = num
        ans = 0

        while 1:
            if numCopy <= 0:
                if ans < 10:
                    break
                else:
                    numCopy = ans
                    ans = 0
            else:
                signle = numCopy % 10  # num的个位数
                ans += signle
                numCopy = numCopy // 10
                # print(ans, signle, numCopy)

        return ans

class Solution2:
     # 2.数学- 数根

     '''
        38 = 3*10 + 8
        38 = 3*(9+1) +8
        38 = 3*9 + 11
        38 = 3*9 + 10 + 1
        38 = 3*9 + 9 + 1 + 1
        38 = 3*9 + 9 + 2
     '''

     def addDigits(self, nums):
        if nums == 0:
            return 0
        else:
            return 1 + (nums - 1) % 9



def randomVerify(ans1:list, ans2:list):

    for i in range(len(ans1)):
        if ans1[i] != ans2[i]:
            print(f'第{i+1}个数字出错')
        else:
            print(f'第{i+1}个正确')


tests = [randint(0, 1000) for i in range(randint(1, 100))]

m1 = Solution1()
m2 = Solution2()

ans1 = [m1.addDigits(test) for test in tests]
ans2 = [m2.addDigits(test) for test in tests]

# print(ans1, ans2)

randomVerify(ans1, ans2)


