def gcp(m, n):
    if n != 0:
        r = m % n
        m = n
        n = r
        return gcp(m, n)
    return m

print(gcp(75,15))
print(gcp(72, 12))
print(gcp(80, 16))