T = int(input())
for _ in range(T):
    A, B = map(int, input().split())

    # A와 B 중에 더 작은 수를 구함
    min_num = min(A, B)
    factor = set()

    for i in range(min_num, 0, -1):
        if A % i == 0 and B % i == 0:
            factor.add(i)
  
    # 최대공약수
    max_f = max(factor)

    # 서로소
    a = A // max_f
    b = B // max_f

    print(max_f * a * b)