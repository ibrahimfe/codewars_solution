def narcissistic( value ):
    digits = len(str(value))
    total = sum(i ** digits for i in map(int, str(value)))
    return True if total == value else False
