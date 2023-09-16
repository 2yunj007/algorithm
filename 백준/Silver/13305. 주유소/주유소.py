# 주유할 때마다 기름 가격을 저장함 (저장된 값보다 더 싸다면)

N = int(input())
road = [0] + list(map(int, input().split()))
oil = list(map(int, input().split()))
cheap_oil = oil[0]

rst = 0
for i in range(1, N):
    rst += road[i] * cheap_oil
    cheap_oil = min(cheap_oil, oil[i])

print(rst)