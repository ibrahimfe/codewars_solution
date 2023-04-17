def friend(x):
    y = []
    a = 0
    for i in x:
        if not i[4]:
            y[a] = i
    return y
