# The One-Liner as Always
def sum_dig_poww(a, b):
    return [
        i
        for i in range(a, b + 1)
        if i == sum(int(digit) ** (index + 1) for index, digit in enumerate(str(i)))
    ]


def sum_dig_pow(a, b):  # range(a, b + 1) will be studied by the function
    result = []
    for i in range(a, b + 1):
        eureka = sum(int(e) ** index for index, e in (enumerate(str(i), start=1)))
        if eureka == i:
            result.append(i)
    return result
