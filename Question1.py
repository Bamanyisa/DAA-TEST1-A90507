def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def insertionSort(A, n):
    for pos in range(1, n):
        nextpos = pos
        while nextpos > 0 and A[nextpos] < A[nextpos - 1]:
            swap(A, nextpos, nextpos - 1)
            nextpos = nextpos - 1
    return A

unsorted_list = [5, 2, 9, 1, 5, 6]

sorted_list = insertionSort(unsorted_list, len(unsorted_list))

