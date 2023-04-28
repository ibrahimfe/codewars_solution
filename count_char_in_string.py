def count(s):
    if s is None or s == "":
        return {}
    dict_1 = {}
    for i in set(s):
        dict_1.update({i : s.count(i)})
    return dict_1
