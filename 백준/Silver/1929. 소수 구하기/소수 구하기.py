import sys
input = sys.stdin.readline

M, N = map(int, input().split())

for i in range(M, N+1):
    chk = True
    # 1은 소수가 아니므로 넘김
    if i == 1:  
        continue
    # 2부터 i의 제곱근까지 나눠 봄
    for j in range(2, int(i**(0.5))+1): 
        # i가 j로 나누어 떨어지면
        if i % j == 0:    
            chk = False
            break
            
    if chk is True:
        print(i)