import math


def find_next_square(sq):
    sq = math.sqrt(sq) + 1
    return sq * sq if sq == int(sq) else -1


print(find_next_square(144))
