# 等差数列差分

# !!!公式
def set(arr, l, r, s, e, d):
    arr[l] += s
    arr[l+1] += d - s
    arr[r+1] -= d + e
    arr[r+2] += e


# 两次前缀和
def build(arr, n):
    for i in range(1, n+1):
        arr[i] += arr[i-1]
    for i in range(1, n+1):
        arr[i] += arr[i-1]
    return arr[1:n+1]

arr = [0 for i in range(10)]
set(arr, 1, 3, 1, 2, 1)
set(arr, 2, 4, 2, 3, 1)
print(build(arr, 9))
