def accum(s):
    s_list = []
    for i in range(1, len(s) + 1):
        s_list.append((s[i -1] * i).capitalize())
    return "-".join(s_list)
