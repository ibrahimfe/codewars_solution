def odd_or_even(arr):
    arr = sum(i for i in arr)
    return "even" if arr == 0 or arr % 2 == 0 else "odd"
