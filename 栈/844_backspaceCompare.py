# 1.比较退格字符串

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        sStack = []
        tStack = []

        for i in s:
            if i == '#' and sStack:
                sStack.pop()
            elif i != '#':
                sStack.append(i)
        
        for i in t:
            if i == '#' and tStack:
                tStack.pop()
            elif i != '#':
                tStack.append(i)

        if sStack == tStack:
            return True
        else:
            return False
    
t = Solution().backspaceCompare("y#fo##f", "y#f#o##f")
print(t)