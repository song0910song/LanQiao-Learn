def brace_match(s):
	match = {'}': '{', ']': '[', ')': '('}
	stack = []

	for ch in s:
		if ch in ['(', '[', '{']:
			stack.append(ch)
		else:
			if len(stack) == 0:
				return False
			t = stack.pop()
			if t != match[ch]:
				return False
	if stack:
		return False
	else:
		return True

ch = '{(}'

s = brace_match(ch)
print(s)
