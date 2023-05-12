def multiplication_table(size):
    list = []
    for i in range(1, size + 1):
        list.append([i * x for x in range(1, size + 1)])
    return list
