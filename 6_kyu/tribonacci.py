def tribonacci(signature, n):
    if n < 3:
        return signature[:n]
    result = signature
    for i in range(3, n):
        result.append(sum(result[i-3:i]))
    return result