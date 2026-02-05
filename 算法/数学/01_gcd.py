# 方法1
def myGcd(a, b):
    return a if b == 0 else myGcd(b, a % b)


# 最小公倍数
def lcm(a, b):
    return a // myGcd(a, b) * b


print(lcm(30, 50))
