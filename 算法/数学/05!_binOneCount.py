'''
递推式 f[i] = f[i/2] + f[i%2]（其中 /表示整数除法）
正是 popcount 的递归定义：
右移一位的 popcount 加上最低位

数列 f的定义实际上就是计算一个数的二进制表示中 1 的个数

求最小的 n'：使得 f[n'] = f[n]，也就是具有相同 popcount 的最小的非负整数。这个数就是 (1 << k) - 1
'''

def binOneCount(n: int):
    # 计算 n 的 popcount
    # bit_count()方法 python 3.8+
    k = n.bit_count()
    # 具有相同 popcount 的最小的非负整数
    n_prime = (1 << k) - 1

    return k, n_prime

t = 100
print(binOneCount(t))
