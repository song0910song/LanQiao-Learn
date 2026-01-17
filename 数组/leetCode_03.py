ls = [1,2,2,4]


'''
reNum = 0
NoNum = 0

for i in range(lenNum):
	if i+1 not in ls:
		NoNum = i+1
	elif ls.count(i+1) > 1:
		reNum = i+1

	if reNum and NoNum != 0:
		break

print([reNum, NoNum])
'''

'''
errorsNum = [0,0]
pre = 0 # 记录先前的数字

for i in range(lenNum):
	curr = ls[i] # 记录当前的数字

	if pre == curr:
		errorsNum[0] = curr # 记录重复的数字
	elif (curr - pre > 1):
		errorsNum[1] = pre + 1 # 记录缺失的数字

	if ls[-1] != lenNum:
		errorsNum[1] = lenNum # 当最后一个数字缺失时

	pre = curr

print(errorsNum)
'''

'''
nums = {}
errorsNum = [0,0]

for i in ls:
	nums[i] = nums.get(i, 0) + 1
	# print(nums)

for i in range(1, len(ls)+1):
	num = nums.get(i, 0)
	# print(num)
	if num == 0:
		errorsNum[1] = i
	elif num > 1:
		errorsNum[0] = i

	if all(errorsNum) != 0:
		# print(errorsNum)
		break
'''

xor_all = 0
for i in range(1, 13 + 1):
    xor_all ^= i
    print(xor_all)
