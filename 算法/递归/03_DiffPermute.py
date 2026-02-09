def permute_unique(arr):
    arr.sort()
    n = len(arr)
    used = [False] * n
    path = [0] * n
    ans = []

    def dfs1(depth):
        if depth == n:
            ans.append(path[:])
            return
        for k in range(n):
            if used[k]:
                continue
            if k > 0 and arr[k] == arr[k - 1] and not used[k - 1]:
                continue
            path[depth] = arr[k]
            used[k] = True
            dfs1(depth + 1)
            used[k] = False
    
    def dfs2(arr, i):
        if i == len(arr):
            ans.append(arr[:])
        
        for j in range(i, n):
            arr[j], arr[i] = arr[i], arr[j]
            dfs2(arr, i+1)
            arr[i], arr[j] = arr[j], arr[i]

    dfs2(arr, 0)
    return ans

arr = [1, 2, 3]
print(permute_unique(arr))
