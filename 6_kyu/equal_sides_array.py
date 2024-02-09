def find_even_index(arr):
    for i in range(0, len(arr)):
        if sum(arr[0:i]) == sum(arr[i + 1 : len(arr) + 1]):
            return i
    return -1
