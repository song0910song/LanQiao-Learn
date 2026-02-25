# 差分

diff = [0] * 501
diff[150] = -1
diff[301] = 1
diff[100] = -1
diff[201] = 1
diff[470] = -1
diff[472] = 1

for i in range(1, 501):
    diff[i] += diff[i-1]

print(diff.count(0))