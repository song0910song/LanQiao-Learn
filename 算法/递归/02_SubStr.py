# 数字组合

from itertools import combinations

# 方法1
def subsetsWithDup(nums):
    """
    返回包含重复元素的数组的所有不重复子集
    """
    def dfs(nums, i, path, size, result):
        """
        :param nums: 排序后的输入数组
        :param i: 当前处理的起始索引
        :param path: 当前路径（组合）
        :param size: 当前路径中的元素个数
        :param result: 结果列表
        """
        if i == len(nums):
            # 到达数组末尾，将当前路径添加到结果中
            result.append(path[:size])
        else:
            # 找到下一组不同数字的起始位置
            j = i + 1
            while j < len(nums) and nums[i] == nums[j]:
                j += 1
            
            # 选择0个当前数字（跳过当前数字组）
            dfs(nums, j, path, size, result)
            
            # 选择1个、2个、3个...当前数字
            for k in range(i, j):
                path[size] = nums[k]  # 添加当前数字到路径
                size += 1
                # 递归处理剩余数字
                dfs(nums, j, path, size, result)

    nums.sort()  # 排序以便处理重复元素
    result = []
    path = [0] * len(nums)  # 预分配路径数组
    dfs(nums, 0, path, 0, result)
    return result

# 测试
nums = [1, 2, 2]
print(subsetsWithDup(nums))
# 输出: [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]