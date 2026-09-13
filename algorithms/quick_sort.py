def quick_sort(arr, l=0, r=None):
    if r == None:
        r = len(arr) - 1

    if l < r:
        pivot = arr[l]
        i = l - 1
        j = r + 1;

        while(True):
            i += 1
            while(arr[i] < pivot):
                yield arr, i, l
                i += 1

            j -= 1
            while(arr[j] > pivot):
                yield arr, j, l
                j -= 1;

            if i >= j:
                break

            arr[i], arr[j] = arr[j], arr[i]
            yield arr, i, j

        yield from quick_sort(arr, l, j)
        yield from quick_sort(arr, j + 1, r)