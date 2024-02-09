def tower_builder(floors):
    return [("*" * (i * 2 + 1)).center(floors * 2 - 1) for i in range(floors)]
