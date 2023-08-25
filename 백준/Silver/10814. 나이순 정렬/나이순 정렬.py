N = int(input())
user = []

for _ in range(N):
    a, b = input().split()
    user.append([int(a), b])

user.sort(key=lambda x:x[0])

for i in user:
    print(*i)