def alternate(n, first_value, second_value):
    return [first_value if idx % 2 == 0 else second_value for idx in range(n)]

