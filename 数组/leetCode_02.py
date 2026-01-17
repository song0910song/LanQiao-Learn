from random import randint

t1 = [1, 1, 0, 1, 1, 1]
t2 = [randint(0,1) for i in range(randint(10,40))]

print(t2)

# zerosNum = t2.count(0)

# # print(zeros)
# maxOnes = 0
# for i in range(zerosNum):

# 	zeroFinded = t2.index(0)

# 	t2 = t2[zeroFinded+1:]

# print(t2)

def maxOneNum(num: list):
	maxOnes = 0
	zerosNum = num.count(0)

	for i in range(zerosNum):
		zeroFinded = num.index(0)

		if len(num[:zeroFinded]) > maxOnes:
			maxOnes = len(num[:zeroFinded])

		num = num[zeroFinded+1:]

	if len(num) > maxOnes:
		maxOnes = len(num)
	
	return maxOnes

print(maxOneNum(t2))