def get_sum(a, b):
    return (
        sum(i for i in range(a, b + 1))
        if a < b
        else sum(i for i in range(b, a + 1))
        if a > b
        else a
    )
    # good luck!
