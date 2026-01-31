# 乒乓球

import sys

txt = sys.stdin.read()

s = ''

for t in txt:
    if t == '\n':
        continue
    elif t == 'E':
        break
    else:
        s += t

a,b = 0, 0
for i in s:
    if i == 'W':
        a += 1
    elif i == 'L':
        b += 1
    
    if (max(a, b) >= 11 and abs(a - b) >= 2):
        print(f'{a}:{b}')
        a, b = 0, 0

print(f'{a}:{b}')
a, b = 0, 0

print()
for i in s:
    if i == 'W':
        a += 1
    elif i == 'L':
        b += 1
    
    if (max(a, b) >= 21 and abs(a - b) >= 2):
        print(f'{a}:{b}')
        a, b = 0, 0

print(f'{a}:{b}')