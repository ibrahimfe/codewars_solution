def high(x):
    x = x.split()
    result = [(sum([ord(char) - 96 for char in i])) for i in x]
    return x[result.index(max(result))]
        
