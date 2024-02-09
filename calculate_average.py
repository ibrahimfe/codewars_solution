def find_average(numbers):
    if not numbers:
        return numbers
    return sum(x for x in numbers) / len(numbers)
