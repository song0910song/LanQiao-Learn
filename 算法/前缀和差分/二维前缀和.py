# 二维前缀和、查询

# 前缀和：prefix[i][j] = matrix[0][0] + ... + matrix[i][j]
def prefix_sum(matrix):
    if not matrix:
        return []
    m, n = len(matrix), len(matrix[0])
    prefix = matrix.copy()
    for i in range(m):
        for j in range(n):
            prefix[i][j] += (prefix[i-1][j] if i > 0 else 0) + (prefix[i][j-1] if j > 0 else 0) - (prefix[i-1][j-1] if i > 0 and j > 0 else 0)
    return prefix

# 查询子矩阵和，左上角(x1, y1)，右下角(x2, y2)
def query(prefix, x1, y1, x2, y2):
    return prefix[x2][y2] - (prefix[x1-1][y2] if x1 > 0 else 0) - (prefix[x2][y1-1] if y1 > 0 else 0) + (prefix[x1-1][y1-1] if x1 > 0 and y1 > 0 else 0)

t = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(prefix_sum(t))
print(query(prefix_sum(t), 0, 0, 1, 1)) # 输出12 (1+2+4+5)


# 列表推导式
t = [[0 for _ in range(3)] for _ in range(3)]
print(t) # 输出[0, 0, 0, 0, 0, 0, 0, 0, 0]
