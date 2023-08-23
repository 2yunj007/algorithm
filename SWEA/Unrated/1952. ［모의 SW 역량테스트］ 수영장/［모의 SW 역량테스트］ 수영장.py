# 부분집합 생성
def powerset(idx):
    global n
    if idx == n:
        m3.append(list(ps))
        return
    # idx 자리의 원소를 뽑고 감
    ps[idx] = 1
    powerset(idx + 1)
    # idx 자리를 안 뽑고 감
    ps[idx] = 0
    powerset(idx + 1)


# ---------------------------------------------
T = int(input())
for tc in range(1, T+1):
    price = list(map(int, input().split())) # 1일, 1달, 3달, 1년 이용권 요금
    plan = list(map(int, input().split()))  # 1년 수영장 이용 계획
    ticket = [0] * 12   # 1년 구매 계획
    total = price[3]  # 최소 비용으로 1년권 가격을 넣어 둠

    # 우선 1일 이용권보다 1달권이 이득일 경우에 대해 생각함
    for i in range(12):
        if plan[i]:
            if  price[1] < price[0] * plan[i]: # 1달권으로 구매하는 것이 이득인 경우
                ticket[i] = price[1]
            else:   # 그렇지 않은 경우
                ticket[i] = price[0] * plan[i]

    s = 0   # 수영장을 처음으로 방문한 달
    e = 0   # 수영장을 마지막으로 방문한 달
    for i in range(11, -1, -1):
        if ticket[i]:
            e = i
            break
    for i in range(12):
        if ticket[i]:
            s = i
            break

    ticket = ticket[s:e+1]
    n = len(ticket)   # 실질적으로 수영장을 이용한 개월 수 (중간에 가지 않은 달 포함)
    ps = [0] * n
    m3 = []     # 3달권을 구매하는 경우의 수
    powerset(0)
    # ticket : [20, 40, 10, 40]
    # m3 : [[1, 1, 1, 1], [1, 1, 1, 0], [1, 1, 0, 1], [1, 1, 0, 0], ...]

    for i in m3:
        t = 0       # 경우의 수에 대한 비용
        use3 = 0     # 3달권 사용 중인지 확인할 변수
        for j in range(n):
            if i[j]:    # 1이면 3달권 가격 더함
                t += price[2]
                use3 = 2    # 3달권 이용 시작 (해당 월에 사용했으므로 미리 1 차감)
            elif use3 > 0:   # 0이고, 현재 3달권 사용 중이라면
                use3 -= 1   # 3달권 차감하고 비용은 더하지 않음
            else:   # 0이고, 3달권 사용이 끝났다면
                t += ticket[j]  # 저장되어 있는 1일권 혹은 1달권의 가격을 더함
        if t < total:   # 현재 최소 비용보다 낮을 경우
            total = t

    print(f'#{tc} {total}')