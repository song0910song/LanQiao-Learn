from itertools import product

def ok(arr):
    n = len(arr)
    for i in range(n):
        # arr[i]=1 诚实者, arr[i]=0 说谎者
        stmt = arr[(i+1)%n] ^ arr[(i+2)%n]  # "后两人一真一假" 的真假
        if arr[i] != stmt:
            return False
    return True

for n in range(1, 13):
    cnt = 0
    liar_sum = 0
    for arr in product([0, 1], repeat=n):
        if ok(arr):
            cnt += 1
            liar_sum += arr.count(0)
    print(f"n={n:2d}  合法方案数={cnt:2d}  说谎者总数={liar_sum}")