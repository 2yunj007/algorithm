from collections import deque
import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
M = int(input())
C = list(map(int, input().split()))

# 스택은 넣었다 빼기만 하니까 고려 안 함
# 큐에 해당하는 원소들은 하나의 이어진 큐라고 생각해도 무방
deq = deque()
for i in range(N):
    if A[i] == 0:
        deq.appendleft(B[i])
# deq에 값이 없을 경우 모두 스택이라는 뜻
# 즉, 수열 C를 그대로 출력
if len(deq) == 0:
    print(*C)
else:   # C의 원소를 deq의 오른쪽에 삽입하고 왼쪽의 값을 pop 및 출력
    for i in C:
        deq.append(i)
        print(deq.popleft(), end=' ')

        
# 시간 초과
# for i in C:
#     tmp = i
#     for j in range(N):
#         if A[j] == 1:   # 자료 구조가 스택이라면 넘어감
#             continue
#         else:   # 자료 구조가 큐라면 i를 해당 인덱스에 삽입하고 기존 원소는 pop
#             tmp, B[j] = B[j], tmp
#     print(tmp, end=' ')