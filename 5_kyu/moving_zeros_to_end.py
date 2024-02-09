def move_zeros(lst):
    result = []
    letter_o = []
    for i in lst:
        if i != 0:
            result.append(i)
        else:
            letter_o.append(i)
    return result + letter_o
