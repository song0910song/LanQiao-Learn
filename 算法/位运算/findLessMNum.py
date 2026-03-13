# 找出少于m次的数

def find_less_m_num(nums, m):
    # 统计每个数的二进制位上1的个数
    bit_count = [0] * 32

    for num in nums:
        for i in range(32):
            bit_count[i] += (num >> i) & 1
    
    # 根据bit_count判断哪个数出现了少于m次
    result = 0
    for i in range(32):
        if bit_count[i] % m != 0:
            result |= (1 << i)
    
    return result

print(find_less_m_num([1, 2, 3, 2, 3, 1, 3, 1], 3))