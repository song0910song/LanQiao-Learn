# 铺地毯

# import sys

# data = sys.stdin.readlines()
# data = [i.rstrip('\n') for i in data]

# n = int(data[0])
# x,y = int(data[-1][0]), int(data[-1][2])

# ans = -1 

# for i in range(1, n+1):
#     a, b, g, k = map(int, data[i].split())
#     if a <= x <= g and b <= y <= k:
#         ans = i
    
# print(ans)
    

n = int(input())
data = []
for i in range(n):
    t = input()
    data.append(t)

x, y = map(int, input().split())

ans = -1

for j,i in enumerate(data):
    a, b, g ,k = map(int, i.split())
    if a <= x <= g+a and b <= y <= k+b:
        ans = j+1

print(ans)