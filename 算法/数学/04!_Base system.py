'''
此题提供一个在不同进制下（2到16），进行加法计算的可能方法
'''


n = int(input()) # 进制
m = input() # 数字

count = 0 # 步骤数

if m == m[::-1]:
    print(f'STEP={count}')
else:
    digits = '0123456789ABCDEF'
    num = m
    for i in range(30):
        re_num = num[::-1]
        to_num1 = [digits.index(ch) for ch in num[::-1]]
        to_num2 = [digits.index(ch) for ch in re_num[::-1]]
        ans = []
        carry = 0 # 进位
        len_arr = max(len(to_num1), len(to_num2))
        
        for j in range(len_arr):
            total = to_num1[j] + to_num2[j] + carry
            ans.append(total % n)
            carry = total // n
        if carry:
            ans.append(carry % n)
        
        num = ''.join([digits[k] for k in ans[::-1]])
        count += 1
        
        if num == num[::-1]:
            print(f"STEP={count}")
            break
            
    else:
        print("Impossible!")