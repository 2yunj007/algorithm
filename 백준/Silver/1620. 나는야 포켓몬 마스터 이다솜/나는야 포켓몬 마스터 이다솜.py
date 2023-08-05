import sys
input = sys.stdin.readline

N, M = map(int, input().split())
pokemon1 = {}   # {번호: 포켓몬 이름}
pokemon2 = {}   # {포켓몬 이름: 번호}

for num in range(1, N+1):    
    name = input().rstrip()
    pokemon1[num] = name
    pokemon2[name] = num

for i in range(M):
    check = input().rstrip()
    if check.isdigit(): # 숫자로 이루어져 있으면
        print(pokemon1[int(check)])
    else:   # 문자열로 이루어져 있으면
        print(pokemon2[check])