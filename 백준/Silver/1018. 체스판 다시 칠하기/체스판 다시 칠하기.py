N, M = map(int,input().split())

wb = 'WB' * 4
bw = 'BW' * 4

# 체스판 만들기
case1 = []
for i in range(4):
    case1.append(wb)
    case1.append(bw)
case2 = []
for i in range(4):
    case2.append(bw)
    case2.append(wb)   

# 보드 불러오기
lst = [input() for _ in range(N)]

# 보드를 돌면서 체스판과 다른 문자들의 수 리스트에 추가
new_color = []
# 보드에 대하여 체스판을 계속 돌리기 위해
for i in range(N - 7):
    for j in range(M - 7):
        count1 = 0
        count2 = 0
        # 보드의 문자와 체스판의 문자가 틀리면 각 케이스별로 카운트 증가
        for h in range(8):
            for w in range(8):
                if lst[i + h][j + w] != case1[h][w]:
                    count1 += 1
                elif lst[i + h][j + w] != case2[h][w]:
                    count2 += 1
        new_color.append(count1)
        new_color.append(count2)
        
print(min(new_color))
