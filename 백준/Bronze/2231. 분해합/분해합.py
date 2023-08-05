'''
 for i : 0부터 N까지 순회:
    if i + i의 각 자릿수의 합 == N:
        i = 생성자
        break (최소 생성자이기 때문)
    if 끝까지 다 돌았는데 없음 i == N:
        0 출력
'''

N = int(input())

for i in range(0, N+1):
    if i + sum(map(int, str(i))) == N:
        print(i)
        break
    if i == N:
        print(0)