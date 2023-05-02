def digital_root(n):
    number = str(n)
    while len(number) > 1:
        number = str(sum(int(i) for i in number))
    return int(number)
