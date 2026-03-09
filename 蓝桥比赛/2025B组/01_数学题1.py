# 题目
'''
小明初始在二维平面的原点(0, 0), 目标点为(233, 666)。小明每次可以选择以下两种方式之一：
1. 沿 x 轴正方向走任意距离。
2. 沿着一个圆心在原点 (0, 0)、以他当前位置到原点的距离为半径的圆的圆周移动，
   移动方向不限（即顺时针或逆时针移动不限）。
'''

import math

def solve() -> None:
    x, y = 233, 666

    # 最优策略：
    # 1) 先沿 x 轴正方向走到 (r, 0)，其中 r = sqrt(x^2 + y^2)
    # 2) 再沿该半径为 r 的圆弧走到目标点 (x, y)
    # 总路程 = r + r * theta, theta = atan2(y, x)
    r = math.hypot(x, y)
    theta = math.atan2(y, x)
    ans = r * (1 + theta)

    # 题目要求四舍五入到整数（0.5 进 1）
    print(int(ans + 0.5))


if __name__ == "__main__":
    solve()
    
