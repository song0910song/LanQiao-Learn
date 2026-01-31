# 神奇的幻方

n = int(input())

m = [[0 for i in range(n)] for j in range(n)]
m[0][n//2] = 1

x,y = 0, n//2

for i in range(2, n*n+1):
    if x == 0 and y != n-1:
        m[n-1][y+1] = i
        x, y = n-1, y+1
    elif x != 0 and y == n-1:
        m[x-1][0] = i
        x, y = x-1, 0
    elif x == 0 and y == n-1:
        m[x+1][y] = i
        x, y = x+1, y
    elif x != 0 and y != n-1:
        if m[x-1][y+1] == 0:
            m[x-1][y+1] = i
            x, y = x-1, y+1
        else:
            m[x+1][y] = i
            x, y = x+1, y

for i in range(n):
    for j in range(n):
        print(m[i][j], end=' ')
    print()
