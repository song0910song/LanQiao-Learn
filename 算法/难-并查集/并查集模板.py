class UnionFind1:
    def __init__(self, n) -> None:
        self.father = list(range(n+1))
        self.size = [1] * (n+1)
        self.stack = []

    def find(self, x: int) -> int:
        size = 0
        # 寻找根节点
        while self.father[x] != x:
            self.stack.append(x)
            x = self.father[x]
            size += 1

        # 路径压缩
        for node in self.stack:
            self.father[node] = x
        self.stack.clear()
        return x
    
    def union(self, a: int, b: int) -> None:
        a = self.find(a)
        b = self.find(b)
        if a == b:
            return
        
        # 小树挂在大树下面
        if self.size[a] < self.size[b]:
            a, b = b, a
        self.father[b] = a
        self.size[a] += self.size[b]

class UnionFind2:
    def __init__(self, n) -> None:
        # 初始化每个节点的父节点为自己
        self.father = list(range(n+1))

    # 查找根节点，并进行路径压缩
    def find(self, x: int) -> int:
        if self.father[x] != x:
            self.father[x] = self.find(self.father[x])
        return self.father[x]
    
    # 将 b 的根节点挂在 a 的根节点下面
    def union(self, a: int, b: int) -> None:
        self.father[self.find(b)] = self.find(a) 


t = UnionFind2(10)
print(t.father)
t.union(1, 2)
t.union(2, 3)
t.union(0, 1)
print(t.father)
print(t.find(2))
print(t.father)