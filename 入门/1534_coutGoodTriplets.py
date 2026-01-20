# 1534. 统计好三元组

from collections import Counter
from typing import List
from random import randint

class Solution:
	def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:

		# 1.暴力破解
		lenNums = len(arr)
		count = 0

		for i in range(lenNums):
			for j in range(i+1, lenNums):
				for k in range(j+1, lenNums):
					if abs(arr[i] - arr[j]) > a or abs (arr[j] - arr[k]) > b or abs(arr[i] - arr[k]) > c:
						continue
					count += 1

		return count

		# 2.




test = [randint(1, 1000) for i in range(randint(3, 101))]
print(test)
print(len(test))

t = Solution().countGoodTriplets([3,0,1,1,9,7], 7, 2, 3)
print(t)


# i**2 - 2*i*j + j**2 = a**2
# j**2 - 2*k*j + k**2 = b**2
# i**2 - 2*i*k + k**2 = c**2


# i**2 +2*k*j-2*i*j -k**2 = a**2 - b**2

# j**2  +2*i*k-2*i*j - k**2 - a**2 - c**2

# j**2 + 2*i*k - 2*k*j - i**2 = b**2 - c**2

# 2*i*k

# i**2 + 2k(j-i) = c**2 - b**2

# k = c**2 - b**2 - i**2 
