def diff_array(arr: list[list[int]], n: int):
    '''

    '''
    # 构建差分数组
    diff = [0 for i in range(n + 1)]
    for row in arr:
        diff[row[0]] += row[2]
        diff[row[1] + 1] -= row[2]

    # 构建前缀和
    for i in range(1, n+1):
        diff[i] += diff[i-1]
    
    return diff[:-1]

print(diff_array([[2, 5, 3], [1, 6, -2], [4, 7, 5]], 9))
