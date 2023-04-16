def grow(arr):
    result = 1
    for (num) in (arr):  # num akan mengambil value yang berada di variable arr hingga ke elemen terakhir
        result *= num
    return result
