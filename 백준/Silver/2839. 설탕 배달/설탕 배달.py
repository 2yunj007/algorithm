N = int(input())
for i in range(N//3+1):
    for j in range(N//5+1):
        if 5*j + 3*i == N:
            print(i + j)
            exit()
print(-1)