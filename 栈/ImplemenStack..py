class Stack:
	def __init__(self):
		self.items = []

	def isEmpty(self):
		return self.items == []

	def push(self, item):
		self.items.append(item)

	def peek(self):
		return self.items[len(self.items) - 1]

	def pop(self):
		return self.items.pop()

	def size(self):
		return len(self.items)

# 测试
t = Stack()
# 添加
t.push(1)
t.push('dog')
print(f"t={t.peek()}")
# 删除
t.pop()
t.pop()
print(f"t是否为空：{t.isEmpty()}")
