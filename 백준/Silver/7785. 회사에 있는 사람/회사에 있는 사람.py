import sys
input = sys.stdin.readline

n = int(input())
logs = {}

for i in range(n):
    name, log = input().split()
    temp = {}
    temp[name] = log
    logs.update(temp)   # 키, 값 추가 / 기존에 키가 있을 시 갱신

# 키, 값을 모은 튜플을 내림차순으로 정렬하고 다시 딕셔너리로 변환
# sorted를 튜플에 사용하면 첫 번째 원소를 기준으로 정렬됨
logs = dict(sorted(logs.items(), reverse=True))


for name in logs:
    if logs[name] == 'enter':   # 현재 enter 상태라면 출력
        print(name)