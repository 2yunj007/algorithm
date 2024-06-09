import sys
input = sys.stdin.readline

M, N = map(int,input().split())

D = [list(map(int,input().strip())) for _ in range(M)]

save = [[0] * (N+2) for _ in range(M+2)]
output = [[0] * (N+2) for _ in range(M+2)]

for i in range(1,M+1):
    output[i][1] = D[i-1][0]

result = 0
for j in range(1,N+1):
    for i in range(1,M+1):
        save[i][j] = max(output[i-1][j-1],output[i][j-1],output[i+1][j-1])
        output[i][j] = save[i][j] + D[i-1][j-1]
        result = max(save[i][j],result)

print(result)