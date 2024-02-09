def sort_array(source_array):
    odd = sorted([n for n in source_array if n % 2 != 0])
    return [odd.pop(0) if n % 2 != 0 else n for n in source_array]
