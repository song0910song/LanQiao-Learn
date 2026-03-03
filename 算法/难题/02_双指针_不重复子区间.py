'''
题目：对于给定的长度为n的数组,找出最长的区间，满足区间中元素两两不同，
如果有多个这样的区间，依次输出它们。
'''

import sys

data = list(map(int, sys.stdin.buffer.read().split()))
n = data[0]
arr = data[1:]

left = 0 # 双指针的左边界
last = [-1] * (n+1) # last[val]记录元素val最近一次出现的位置，初始为-1表示未出现过
max_num = 0
len_arr = len(arr)
ans_arr = []
for right in range(len_arr):
    val = arr[right]
    # 如果当前元素val之前出现过，并且上次出现的位置在当前左边界之后，说明区间内有重复元素，需要移动左边界
    if last[val] != -1 and last[val] >= left:
        left = last[val] + 1
    cur = right - left + 1
    if cur > max_num:
        max_num = cur
        ans_arr = [(left+1, right + 1)]
    elif cur == max_num:
        ans_arr.append((left+1, right+1))
    # 更新最近出现的位置
    last[val] = right 

out = [str(len(ans_arr))]
for l, r in ans_arr:
    out.append(f"{l} {r}")
sys.stdout.write("\n".join(out))
    