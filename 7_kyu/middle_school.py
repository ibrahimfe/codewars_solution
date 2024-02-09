def largest_prime_factor(n):
    i = 2
    arr = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            arr.append(n)
    return arr

print(largest_prime_factor(75))