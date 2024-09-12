def merge(arr1, arr2):
    m, n = len(arr1), len(arr2)
    temp = arr1 + arr2
    arr1[:] = [0] * (m + n)
    arr2[:] = [0] * (m + n)
    
    i, j, k = m - 1, n - 1, m + n - 1

    while i >= 0 and j >= 0:
        if temp[i] > temp[j]:
            arr1[k] = temp[i]
            i -= 1
        else:
            arr1[k] = temp[j]
            j -= 1
        k -= 1

    while j >= 0:
        arr1[k] = temp[j]
        j -= 1
        k -= 1

    arr2[:] = temp[i + 1:m + n]

    return arr1, arr2
arr1 = [1, 3, 5]
arr2 = [2, 4, 6]
merge(arr1, arr2)
print("arr1 =", arr1)
print("arr2 =", arr2)
