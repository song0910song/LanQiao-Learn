# 验证栈序列

pushed = [1,2,3,4,5]
popped = [4,5,3,2,1]

stack = []
index = 0

for i in pushed:
    stack.append(i)
    print("add:")
    print(stack)
    while popped[index] == stack[-1]:
        stack.pop()
        print("del:")
        print(stack)
        index += 1

        if index == len(popped):
            break

if stack:
    print('1')

from typing import List

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        valid_stack = []
        index = 0

        for i in pushed:
            valid_stack.append(i)

            while valid_stack and popped[index] == valid_stack[-1]:
                valid_stack.pop()
                index += 1
                if index == len(popped):
                    break
        if valid_stack:
            return False
        return True
    
t = Solution().validateStackSequences([1,0], [1,0])
print(t)