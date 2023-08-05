'''
for 첫 번째 카드 : 0 -> N - 2:
    for 두 번째 카드 : 첫 번째 카드 한 칸 앞 -> N - 1:
        for 세 번째 카드 : 두 번째 카드 한 칸 앞 -> N:
                세 장의 카드를 더함

            if M보다 작거나 같음 and 현재 저장된 3장의 합보다 큼:
                총합의 값 바꿔 줌
'''    

N, M = map(int, input().split())
cards = list(map(int, input().split()))

black = 0

for i in range(0, N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            sum_v = cards[i] + cards[j] + cards[k]

            if black < sum_v <= M:
                black = sum_v

print(black)