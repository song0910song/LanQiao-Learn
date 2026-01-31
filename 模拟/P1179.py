# 数字统计

l, r = map(int, input().split())

count = 0

for i in range(l, r+1):
    while i != 0:
        t = i % 10
        if t == 2:
            count += 1
        i //= 10

print(count)