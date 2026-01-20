# 中序表达式转后续表达式

import string

def infixToPostfix(infixexper):
	pre = {"*": 3, "/": 3, "+": 2, "-": 2, "(": 1} # 运算符优先级
	onStack = [] # 暂存运算符
	postfixexper = [] # 后序表达式

	tokenList = infixexper.split()
	# print(tokenList)

	for token in tokenList:

		if token in string.ascii_uppercase:
			postfixexper.append(token) # 操作数

		elif token == '(':
			onStack.append(token) # 运算符
		
		elif token == ')':
			t = onStack.pop()
			while t != '(':
				postfixexper.append(t)
				t = onStack.pop()
		else:
			# 如果优先级比栈中的要高，弹出并放入前序表达式列表中
			# print(onStack)
			while (len(onStack) != 0 and pre[onStack[-1]] >= pre[token]):
				postfixexper.append(onStack.pop())
			onStack.append(token) # 栈入运算符
		# print(postfixexper)

	while len(onStack) != 0:
		postfixexper.append(onStack.pop())

	return " ".join(postfixexper)

t = infixToPostfix("( A + B ) * ( C + D )")
print(t)


