
# 向上调整
def heapInsert(arr, i):
    while (arr[i] > arr[int((i - 1)/2)]):
        arr[int((i - 1)/2)], arr[i] = arr[i], arr[int((i - 1)/2)]
        i = int((i - 1)/2)

# 向下调整
def heapify(arr, i, size):
    # 左节点
    l = i * 2 + 1
    while (l < size):
        # 右节点
        # 评选 
        # 1. 左节点值与右节点比较
        best = l + 1 if l + 1 < size and arr[l] < arr[l+1] else l
        # 2.最大节点的值与父节点比较
        best = best if arr[best] > arr[i] else i

        if (best == i):
            break

        arr[i], arr[best] = arr[best], arr[i]
        i = best
        l = i * 2 + 1

# 堆排序(从顶到低)
def heapSort1(arr):
    n = len(arr)
    # 向上调整
    for i in range(n):
        heapInsert(arr, i)

    size = n
    while (size > 1):
        arr[0], arr[size - 1] = arr[size - 1], arr[0]
        size -= 1
        heapify(arr, 0, size)


# 堆排序(从低到顶)
def heapSort2(arr):
    n = len(arr)
    for i in range(int((n-2)/2), -1, -1):
        heapify(arr, i, n)

    size = n
    while (size > 1):
        arr[0], arr[size - 1] = arr[size - 1], arr[0]
        size -= 1
        heapify(arr, 0, size)

t = [5, 2, 3, 4, 9, 1, 0]
s = heapSort2(t)
print(t)