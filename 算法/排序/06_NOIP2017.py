# 图书管理员

import sys

n, q = map(int, input().split())
book_id = []
need_id = []
i = 0
j = 0
for line in sys.stdin:
    if i < n:
        book_id.append(line.strip('\n'))
    else:
        need_id.append(line.strip('\n').split())
        j+=1
    i += 1
    
book_id.sort(key=lambda a:(len(a), a))

for i in need_id:
    flag = 1
    t = int(i[0])
    for j in range(n):
        if book_id[j][-t:] == i[1]:
            print(book_id[j])
            flag = 0
            break
    if flag:
        print('-1')
