from itertools import product


def solution(users, emoticons):
    answer = [0, 0]
    n = len(users)
    m = len(emoticons)
    discounts = [10, 20, 30, 40]
    
    # 이모티콘 할인율 선택
    select_discount = product(discounts, repeat=m)  # 중복 순열
    for discount in select_discount:
        sub = 0     # 가입자 수
        sales = 0   # 매출액
        
        for i in range(n):
            # i번째 고객의 구매 기준
            rate, price = users[i][0], users[i][1]
            total_price = 0
            
            for j in range(m):
                # 구매 기준에 맞는 할인율일 경우
                if discount[j] >= rate:
                    total_price += int(emoticons[j] * (100 - discount[j]) * 0.01)
            
            # 구매한 이모티콘의 총 금액이 구매 기준 비용 이상일 경우 플러스 가입자 수 증가
            if total_price >= price:
                sub += 1
            else:   # 이내일 경우 매출액 증가
                sales += total_price
        
        # 목표 조건에 따라 갱신
        if sub > answer[0] or sub == answer[0] and sales > answer[1]:
            answer = [sub, sales]
                
    return answer