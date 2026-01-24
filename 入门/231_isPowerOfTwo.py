# 231. 2 的幂

import math

class Solution:
	def __init__(self, n: int):
		self.n = n

	def isPowerOfTwoMethod1(self) -> bool:
		# log2(n) 的指数不能小于等于0
		if self.n <= 0:
			return False

		x = math.log2(self.n)
		return x.is_integer()

	def isPowerOfTwoMethod2(self) -> bool:
		# 位运算：n & (n - 1) == 0 则为 2 的幂
		if self.n <= 0:
			return False
		return (self.n & (self.n - 1)) == 0

	def isPowerOfTwoMethod3(self) -> bool:
		# 判断是否是2^31的倍数
		maxN = pow(2, 31)

		if self.n > 0:
			return (maxN / self.n).is_integer()
		else:
			return False


t = Solution(-16).isPowerOfTwoMethod3()
print(t)



