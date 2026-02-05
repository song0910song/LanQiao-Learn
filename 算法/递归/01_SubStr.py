# 子字符串


# 1.方法一
def f(s: str, i: int, path: list[str], size: int):
    '''
    :param s: 字符串
    :type s: str
    :param i: 字符串下标索引
    :type i: int
    :param path: 储存字符串
    :type path: list[str]
    :param size: path数组大小
    :type size: int
    '''

    if i == len(s):
        ans.append("".join(path[:size]))
    else:
        path[size] = s[i]
        f(s, i + 1, path, size + 1)
        f(s, i + 1, path, size)

# 方法二
from itertools import combinations
def substr(s:str, i:int) -> list[str]:
    arr = []
    for j in range(0, i+1):
        sub = combinations(s, j)
        sub = [''.join(k) for k in sub]
        arr.extend(sub)
    return arr


s = "abc"
path = [''] * len(s)
ans = []
f(s, 0, path, 0)
m2 = substr(s, 3)
print(ans)
print(m2)