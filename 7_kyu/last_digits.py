def solution(n, d):
    # your code here
    return list(map(int, list(str(n))))[-d:] if d > 0 else []
