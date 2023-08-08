arr = [[0] * 100 for i in range(100)]
N = int(input())    # 색종이의 수

for _ in range(N):
    x, y = map(int, input().split())
    
    # 색종이의 범위만큼 배열에 1을 더함
    for i in range(90-y, 100-y):
        for j in range(x, x+10):
            arr[i][j] += 1

cnt = 0
for i in range(100):
    for j in range(100):
        # 0이 아닐 경우, 종이가 붙어 있다는 뜻
        if arr[i][j] != 0:
            cnt += 1

print(cnt)