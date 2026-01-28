# 生活大爆炸版石头剪刀布

n, n_a, n_b = map(int, input().split())
a_nums = list(map(int, input().split()))
b_nums = list(map(int, input().split()))

scores = [0, 0]

for i in range(n):
    a = i % n_a
    b = i % n_b

    if (a_nums[a] == 0 and b_nums[b] in [2, 3]) or (a_nums[a] == 1 and b_nums[b] in [0, 3]) or (a_nums[a] == 2 and b_nums[b] in [4, 1]) \
        or (a_nums[a] == 3 and b_nums[b] in [2, 4]) or (a_nums[a] == 4 and b_nums[b] in [0, 1]):
        scores[0] += 1
    elif (b_nums[b] == 0 and a_nums[a] in [2, 3]) or (b_nums[b] == 1 and a_nums[a] in [0, 3]) or (b_nums[b] == 2 and a_nums[a] in [4, 1]) \
        or (b_nums[b] == 3 and a_nums[a] in [2, 4]) or (b_nums[b] == 4 and a_nums[a] in [0, 1]):
        scores[1] += 1


print(*scores)