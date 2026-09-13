def merge(arr, l, m, r):
    n = m - l + 1
    n1 = r - m

    A = arr[l:m+1]
    B = arr[m+1:r+1]

    i, j = 0, 0
    k = l

    while i < n and j < n1:
        yield arr, l + i, m + 1 + j
        if A[i] < B[j]:
            yield arr, l + i, k
            arr[k] = A[i]
            i += 1
        else:
            yield arr, l + j, k
            arr[k] = B[j]
            j += 1
        k += 1

    while(i < n):
        yield arr, l + i, k
        arr[k] = A[i]
        i += 1
        k += 1;

    while(j < n1):
        yield arr, l + j, k
        arr[k] = B[j]
        j += 1;
        k += 1;

def merge_sort1(arr, l, r):
    if l >= r:
        return
    m = (l + r)//2
    yield from merge_sort1(arr, l, m)
    yield from merge_sort1(arr, m+1, r)
    yield from merge(arr, l, m, r)

def merge_sort(arr):
    yield from merge_sort1(arr, 0, len(arr) - 1)
