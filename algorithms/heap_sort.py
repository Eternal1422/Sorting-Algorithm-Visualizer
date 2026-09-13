def heapify(arr, n, i):
    maxn = i
    l = 2 * i + 1
    r = 2 * i + 2

    if(l < n):
        yield arr, l, maxn 
        if(arr[l] > arr[maxn]):
            maxn = l

    if(r < n):
        yield arr, r, maxn 
        if(arr[r] > arr[maxn]):
            maxn = r

    if(maxn != i):
        arr[i], arr[maxn] = arr[maxn], arr[i]
        yield arr, i, maxn
        yield from heapify(arr, n, maxn)

def heap_sort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        yield from heapify(arr, n, i)

    for i in range(n - 1, -1, -1):
        arr[0], arr[i] = arr[i], arr[0]
        yield arr, 0, i
        yield from heapify(arr, i, 0)