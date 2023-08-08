# 소수를 판별하는 함수
def PrimeCheck(n):
        if n == 0 or n == 1:
             return False
        # N^(1/2)까지만 나눠서 소수 판별
        for i in range(2, int(n**(1/2))+1):
            if n % i == 0:
                return False
        return True


T = int(input())
for _ in range(T):
    n = int(input())
    
    while True:
        # 소수면 출력
        # n보다 크거나 같은 소수: 처음 발견한 소수를 출력하면 됨
        if PrimeCheck(n):   
            print(n)
            break
        else:
            n += 1