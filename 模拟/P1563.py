# 玩具谜题

n, m = map(int, input().split())

r, string = [], []

for i in range(n):
    t_r, t_string = input().split()
    r.append(int(t_r))
    string.append(t_string)

index = n # 玩具人下标

for i in range(m):
    a, s = map(int, input().split()) # 朝向，步数

    if index <= 0:
        index = n
    
    # 朝里
    if r[index % n] == 0:
        # 左
        if a == 0:
            index = (index - s) % n
        # 右 
        else:
            index = (index + s) % n
    else:
        if a == 0:
            index = (index + s) % n
        else:
            index = (index - s) % n

print(string[index])

