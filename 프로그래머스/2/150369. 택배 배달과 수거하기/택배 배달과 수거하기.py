def solution(cap, n, deliveries, pickups):
    answer = 0

    # 예외 처리 (배달/수거할 상자가 하나도 없을 경우 testcase 2)
    if set(deliveries) == {0} and set(pickups) == {0}:
        return answer
    
    sd, sp = n - 1, n - 1  # 배달/수거 시작 지점

    while sd >= 0 or sp >= 0:
        tmp = [0, 0]

        if sd >= 0:  # 배달할 상자가 남아 있는 경우
            update = False
            cnt = 0
            completion = False
            for i in range(sd, -1, -1):
                # 시작 지점 업데이트 (상자가 존재하기 시작하는 구간)
                if not update and deliveries[i]:
                    sd = i
                    tmp[0] = i
                    update = True
                elif not update and not deliveries[i]:
                    continue

                # 먼 집부터 배달할 상자 수를 카운트
                cnt += deliveries[i]
                deliveries[i] = 0

                if cnt > cap:  # 수용량보다 많아졌을 때 다음 턴에 i 번째 집부터 방문
                    sd = i
                    deliveries[i] = cnt - cap
                    break
            else:  # 배달할 상자가 없었다면
                sd = -1

        if sp >= 0:  # 수거할 상자가 남아 있는 경우
            update = False
            cnt = 0
            completion = False
            for i in range(sp, -1, -1):
                if not update and pickups[i]:
                    sp = i
                    tmp[1] = i
                    update = True
                elif not update and not pickups[i]:
                    continue

                cnt += pickups[i]
                pickups[i] = 0

                if cnt > cap:
                    sp = i
                    pickups[i] = cnt - cap
                    break
            else:
                sp = -1

        # 두 시작 지점 중 더 큰 수 * 2를 answer에 더함
        answer += (max(tmp) + 1) * 2

    return answer