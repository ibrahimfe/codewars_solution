def positive_sum(arr):
    # Your code here
    sop = 0
    x = len(arr)
    for i in range(0, x):
        if arr[i] >= 0:
            sop += arr[i]
    print(sop)
    return 0
