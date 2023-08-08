An ,Ad = map(int, input().split())
Bn, Bd = map(int, input().split())

n = Bn*Ad + An*Bd   # 분자
d = Ad*Bd   # 분모

# 분자와 분모를 최대공약수로 나누면 기약분수가 됨
# 유클리드 호제법
num = max(n, d)
f = min(n, d)
max_f = 0

while True:
    if num % f == 0:    
        max_f = f
        break
    else:
        num, f = f, num % f

print(n//max_f, d//max_f)