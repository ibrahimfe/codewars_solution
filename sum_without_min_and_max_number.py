def sum_array(arr):
    if arr is None or len(arr) <= 2:
        return 0
    min_value = min(arr)
    max_value = max(arr)

    return sum(arr) - min_value - max_value
