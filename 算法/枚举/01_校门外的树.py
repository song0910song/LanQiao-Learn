# 题目链接：https://ac.nowcoder.com/acm/contest/20960/1010
# 两种方法：1.差分  2.区间合并（新，快）
# 题目描述：校门外有一排树，树的编号从0到n。现在有q个区间，
# 每个区间表示被占用的树的范围。请问剩余未被占用的树的数量。

# 1.差分
def diff_method(len, q, q_arr):
    diff = [0] * (len + 2)
    for i in range(q):
        l, r = q_arr[i][0], q_arr[i][1]
        diff[l] -= 1
        diff[r + 1] += 1
    
    t = 0
    ans = 0
    for i in range(len + 1):
        t += diff[i]
        if t == 0:
            ans += 1
    
    return ans

# 2.区间合并
def inter_combin(len, q, q_arr):
    # 排序，便于区间的延展
    arr_sorted = sorted(q_arr, key=lambda x:(x[0], x[1]))
    current_l = arr_sorted[0][0]
    current_r = arr_sorted[0][1]

    ans = 0
    for i in range(1, q):
        left, right = arr_sorted[i][0], arr_sorted[i][1]
        if left <= current_r:
            current_r = max(current_r, right)
        elif left > current_r:
            ans += current_r - current_l + 1
            current_l, current_r = left, right
    
    # 计算最后一次区间
    ans += current_r - current_l + 1

    return len + 1 - ans

# 对数器
def validate():
    import random
    for _ in range(1000):
        len = random.randint(1, 100)
        q = random.randint(1, 20)
        q_arr = []
        for _ in range(q):
            l = random.randint(0, len - 1)
            r = random.randint(l, len - 1)
            q_arr.append((l, r))
        
        ans1 = diff_method(len, q, q_arr)
        ans2 = inter_combin(len, q, q_arr)
        if ans1 != ans2:
            print("Error!")
            print(f"len: {len}, q: {q}, q_arr: {q_arr}")
            print(f"ans1: {ans1}, ans2: {ans2}")
            break
    else:
        print("通过测试")

validate()