# 给定一个数组arr和一个整数aim，求arr的最长子数组长度，要求子数组累加和等于aim

def longest_subarray_sum_equal_is_aim(arr, aim):
    # key: 前缀和 
    # value: 前缀和最早出现的位置
    sum_map = {0:-1}
    ans = 0
    # 前缀和
    sum_arr = 0

    for i in range(len(arr)):
        sum_arr += arr[i]
        if sum_map.get(sum_arr - aim) is not None:
            ans = max(ans, i - sum_map[sum_arr - aim])
        if sum_arr not in sum_map:
            sum_map[sum_arr] = i

    return ans

t = [3, 2, -5, 6, 2, 1]
print(longest_subarray_sum_equal_is_aim(t, 5))