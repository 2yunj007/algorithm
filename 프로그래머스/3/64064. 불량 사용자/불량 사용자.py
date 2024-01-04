import re

def solution(user_id, banned_id):
    matching = {}
    
    for pattern in banned_id:
        # 패턴과 일치하는 유저 목록
        matching.setdefault(pattern, [])     
        
    for pattern in matching:
        # 정규 표현식 패턴 컴파일
        pattern_re = re.compile(pattern.replace('*', '.'))
        
        for user in user_id:
            # 컴파일된 패턴과 유저 id가 매칭되면 append
            # 이때 길이를 확인하지 않으면 abc와 abcd가 같은 패턴으로 추가됨
            if len(pattern) == len(user) and pattern_re.match(user):    
                matching[pattern].append(user)

    
    def recur(i, matching_lst):
        global answer
        # 불량 사용자를 모두 매칭시킨 경우
        if i == len(banned_id):
            # matching_lst(불량 사용자 목록)에 추가된 순서를 고려하지 않기 위해 set로 변환
            matching_set = set(matching_lst)
            # 아직 결과 리스트에 추가되지 않은 조합이라면 append
            if matching_set not in matching_result:
                matching_result.append(matching_set)
            return
        
        pattern = banned_id[i]
        for user in matching[pattern]:
            # 매칭 리스트에 이미 있는 경우 pass
            if user in matching_lst:
                continue
            # 아닌 경우 recur
            recur(i + 1, matching_lst + [user])
    
    
    matching_result = []
    recur(0, [])
    answer = len(matching_result)
                
    return answer