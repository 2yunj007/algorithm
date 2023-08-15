# 에라토스테네스의 체
primes = [1] * 1000001
for i in range(2, 1000001):
    if primes[i]:
        for j in range(2*i, 1000001, i):
            primes[j] = 0

T = int(input())
for _ in range(T):
    N = int(input())
    cnt = 0
    for i in range(2, N//2+1):  # 중복 방지를 위해 N//2까지 반복
        if primes[i] and primes[N-i]:   # i도 소수면서 N-i도 소수라면
            cnt += 1
    print(cnt)