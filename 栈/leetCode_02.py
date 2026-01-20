
from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        NumsStack = [] # 数字栈
        NumTokens = len(tokens)

        for i in range(NumTokens):
        	if len(tokens) < 2:
        		NumsStack.append(int(tokens))
        		break
        	else:
        	 if tokens[i] == '+':
        	 	t1 = int(NumsStack.pop())
        	 	t2 = int(NumsStack.pop())
        	 	NumsStack.append(t2 + t1)
        	 elif tokens[i] == '/':
        	 	t1 = int(NumsStack.pop())
        	 	t2 = int(NumsStack.pop())
        	 	NumsStack.append(t2 // t1)
        	 elif tokens[i] == '*':
        	 	t1 = int(NumsStack.pop())
        	 	t2 = int(NumsStack.pop())
        	 	NumsStack.append(t2 * t1)
        	 elif tokens[i] == '-':
        	 	t1 = int(NumsStack.pop())
        	 	t2 = int(NumsStack.pop())
        	 	NumsStack.append(t2 - t1)
        	 else:
        	 	NumsStack.append(tokens[i])

        return NumsStack[0]

t = Solution().evalRPN(["4", "13", "5", "/", "+"])
print(t)