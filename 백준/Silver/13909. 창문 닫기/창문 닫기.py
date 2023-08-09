N = int(input())
print(int(N**(0.5)))

'''
N: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
   1 1 1 2 2 2 2 2 3  3  3  3  3  3  3  4
   => 루트 씌우고 소수점 버리면 나옴
'''
# 완탐; 메모리 초과; 근데 이걸로 규칙성 찾음
# window = {}
# for i in range(1, N+1):
#     window[i] = 0   # {1: 0, 2: 0, 3: 0}

# for i in range(1, N+1): # 창문 범위
#     for j in range(i, N+1, i):  # i의 배수만큼 동작
#         # 열려 있으면 닫고, 닫혀 있으면 엶
#         if window[j] == 1:
#             window[j] = 0
#         else:
#             window[j] = 1

# print(sum(window.values()))
