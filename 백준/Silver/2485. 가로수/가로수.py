import sys
input = sys.stdin.readline

# 최대공약수 구하는 함수
def Euclid(num, f):
    while True:
        if num % f == 0:    
            max_f = f
            return max_f
        else:
            num, f = f, num % f


# 소수인지 판별하는 함수
def PrimeCheck(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


N = int(input())
tree = [int(input()) for _ in range(N)]    # 가로수 위치

step = set()   # 가로수 사이의 간격 / 중복 제거를 위해 set 사용
for i in range(len(tree)-1):
    step.add(tree[i+1] - tree[i])
step = list(step)

# a, b, c가 있을 때
# a와 b의 최대공약수 x를 계산하고
# x와 c의 최대공약수를 구하면 그 수가 a, b, c의 최대공약수

max_f = step[0] # 최대공약수
for i in range(1, len(step)):
    max_f = Euclid(step[i], max_f)
    # 최대공약수가 소수이면 더 계산할 필요 없음
    if PrimeCheck(max_f) is True:
        break

result = (tree[-1] - tree[0]) // max_f - N + 1
print(result)