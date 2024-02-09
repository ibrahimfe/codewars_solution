def cic(m,n):
    t = min(m,n)
    r = m % n
    
    if r == 0:
        r = n % t
        if r == 0:
            return t
    t -= 1
    return cic(m,n)

print(cic(75, 15))
print(cic(72, 12))
print(cic(80, 16))