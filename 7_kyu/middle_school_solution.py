def calculate_prime_factors(x):
    prime_factors = set()
    if N % 2 == 0:
        prime_factors.add(2)
    while N % 2 == 0:
        N = N // 2
        if N == 1:
            return prime_factors
    for factor in range(3, N + 1, 2):
        if N % factor == 0:
            prime_factors.add(factor)
            while N % factor == 0:
                N = N // factor
                if N == 1:
                    return prime_factors