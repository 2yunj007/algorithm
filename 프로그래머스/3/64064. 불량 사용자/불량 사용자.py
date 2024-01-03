import re

def solution(user_id, banned_id):
    matching = {}
    
    for pattern in banned_id:
        # 패턴에 해당하는 유저 수
        matching.setdefault(pattern, [])     
        
    for pattern in matching:
        # 정규 표현식 패턴 컴파일
        pattern_re = re.compile(pattern.replace('*', '.'))
        
        # 매칭되는 유저
        for user in user_id:
            # 패턴과 유저 id가 매칭되면
            if pattern_re.match(user) and len(pattern) == len(user):
                matching[pattern].append(user)

    
    def f(i, matching_lst):
        global answer
        if i == len(banned_id):
            matching_set = set(matching_lst)
            if matching_set not in matching_result:
                matching_result.append(matching_set)
            return
        
        pattern = banned_id[i]
        for user in matching[pattern]:
            # 매칭 리스트에 이미 있는 경우 pass
            if user in matching_lst:
                continue
            # 아닌 경우 recur
            f(i + 1, matching_lst + [user])
    
    
    matching_result = []
    f(0, [])
    answer = len(matching_result)
                
    return answer