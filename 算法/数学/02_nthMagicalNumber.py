from math import lcm

def nthMagicalNumber(n, a, b):
    r = n * min(a, b)
    l = 0
    ans = 0

    while l <= r:
        m = (l + r) // 2
        if (m // a + m // b - m // lcm(a, b) >= n):
            ans = m
            r = m - 1
        else:
            l = m + 1
    return int(ans % (1e9 + 7))

print(nthMagicalNumber(1000000000, 40000, 40000))
