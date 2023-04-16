def check_case(char1, char2):
    if not char1.isalpha() or not char2.isalpha():
        return -1
    elif char1.islower() == char2.islower():
        return 1
    else:
        return 0
