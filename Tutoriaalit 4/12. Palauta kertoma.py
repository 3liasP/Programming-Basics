def kertoma(n: int) -> int:
    fact = 1
    for i in range(1,n+1):
        fact = fact * i
    n = fact
    return n

print(kertoma(5))