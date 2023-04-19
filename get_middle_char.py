def get_middle(s):
    middle_index = len(s) // 2
    if len(s) % 2 != 0:
        return s[middle_index]
    else:
        return s[middle_index - 1] + s[middle_index]
