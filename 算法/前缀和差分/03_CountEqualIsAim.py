# 给定一个数组arr和一个整数aim，返回arr中有多少个子数组的累加和等于aim

from random import randint

def Count_EqualIsAim(arr: list[int], aim: int):
    # key: 前缀和 
    # value: 前缀和出现的次数
    sum_map = {0:1}
    ans = 0
    # 前缀和
    sum_arr = 0

    for i in range(len(arr)):
        sum_arr += arr[i]
        ans += sum_map.get(sum_arr - aim, 0)
        sum_map[sum_arr] = sum_map.get(sum_arr, 0) + 1

    return ans

def Count_EqualIsAim2(arr: list[int], aim: int):
    ans = 0
    len_arr = len(arr)

    '''
        例
        [ 3, 2, -5, 6, 2, 1 ]
        
        3
        i,j
        sum_arr = 3

        3, 2
        i  j
        sum_arr = 3 + 2 = 5

        3, 2, -5
        i      j
        sum_arr = 3 + 2 - 5 = 0

        ......

    '''

    for i in range(len_arr):
        for j in range(i, len_arr):
            sum_arr = 0
            for k in range(i, j+1):
                sum_arr += arr[k]

            if sum_arr == aim:
                ans += 1

    return ans


def validate():
    for i in range(1000):
        arr = [randint(-100, 100) for _ in range(randint(1, 20))]
        aim = randint(-100, 100)
        print("arr is: ", arr)

        m1 = Count_EqualIsAim(arr, aim)
        m2 = Count_EqualIsAim2(arr, aim)
        if Count_EqualIsAim(arr, aim) != Count_EqualIsAim2(arr, aim):
            print("Missive mistake!!!")
            print(m1)
            print(m2)
            break
    else:
        print('the test is pass!!!')

validate()