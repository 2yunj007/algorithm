def solution(n, times):
    answer = 0
    
    start = min(times) * n // len(times)
    end = max(times) * n    # 최악의 경우
    
    while start <= end:
        people = 0
        # mid 시간 동안 입국 심사가 가능한지 판단
        # 즉, mid 시간 동안 각 심사관이 몇 명을 처리할 수 있는가?
        mid = (start + end) // 2
        
        for time in times:
            # 입국 심사가 가능한 사람 수
            people += mid // time
        
        # n과 같거나 더 많은 인원 수용이 가능한 경우
        # 일단 answer에 저장 하고 시간을 더 줄여 봄
        if people >= n:
            answer = mid
            end = mid - 1
        # n명의 인원을 수용하지 못하는 경우
        # 시간을 늘려야 함
        else:
            start = mid + 1
    return answer