A, B = map(int, input().split())

max_f = 0   # 최대공약수

# 유클리드 호제법
while True:
    # 나누어 떨어지게 하는 수가 최대공약수
    if num % f == 0:    
        max_f = f
        break
    # 나누어 떨어지지 않으면, 그 나머지로 현재 나누어지는 수(f)를 나눠야 함
    else:
        num, f = f, num % f
    
a = A // max_f
b = B // max_f
print(a * b * max_f)