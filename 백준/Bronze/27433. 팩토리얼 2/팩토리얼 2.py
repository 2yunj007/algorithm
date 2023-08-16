def factorial(N):
    if N < 2:
        return 1
    else:
        return N * factorial(N-1)


N = int(input())
print(factorial(N))