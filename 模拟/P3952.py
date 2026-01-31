def solve():
    t = int(input().strip())
    
    for _ in range(t):
        # 读取程序长度和声称的复杂度
        line = input().strip()
        while line == '':
            line = input().strip()
        L, comp_str = line.split()
        L = int(L)
        
        # 解析声称的复杂度 O(1) -> 0, O(n^w) -> w
        if comp_str == "O(1)":
            claimed_power = 0
        else:
            claimed_power = int(comp_str.split('^')[1].rstrip(')'))
        
        stack = []          # 栈元素: (变量名, factor, 是否执行)
        variables = set()   # 当前作用域内的变量
        current_power = 0   # 当前复杂度指数
        max_power = 0       # 最大复杂度指数（答案）
        dead_count = 0      # 当前处于多少层dead循环中
        err = False
        
        for _ in range(L):
            line = input().strip()
            if err:
                continue    # 已报错，仍需读完输入
            
            if line[0] == 'F':
                _, var, x, y = line.split()
                
                # 语法检查1：变量重名
                if var in variables:
                    err = True
                    continue
                
                # 计算当前循环的factor和是否执行
                if x == 'n' and y == 'n':
                    factor, is_alive = 0, True      # 执行1次
                elif x == 'n':  # y是常数
                    factor, is_alive = 0, False     # n > 常数，不执行
                elif y == 'n':  # x是常数
                    factor, is_alive = 1, True      # O(n)
                else:  # 都是常数
                    xi, yi = int(x), int(y)
                    if xi <= yi:
                        factor, is_alive = 0, True
                    else:
                        factor, is_alive = 0, False
                
                # 更新复杂度：只有当前不在dead区域内且本层alive才累加
                if is_alive:
                    if dead_count == 0:
                        current_power += factor
                        max_power = max(max_power, current_power)
                else:
                    dead_count += 1
                
                stack.append((var, factor, is_alive))
                variables.add(var)
                
            else:  # 'E'
                if not stack:
                    err = True  # 语法错误：E无匹配
                    continue
                
                var, factor, is_alive = stack.pop()
                variables.remove(var)
                
                # 退栈时恢复状态
                if is_alive:
                    if dead_count == 0:
                        current_power -= factor
                else:
                    dead_count -= 1
        
        # 最终判断
        if err or stack:  # stack非空表示有F未匹配
            print("ERR")
        else:
            print("Yes" if max_power == claimed_power else "No")

if __name__ == "__main__":
    solve()