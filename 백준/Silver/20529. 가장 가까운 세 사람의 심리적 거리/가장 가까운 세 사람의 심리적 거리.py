import sys
input = sys.stdin.readline
from itertools import combinations


'''
비둘기 집 원리
: N마리의 비둘기와 M개의 둥지가 있을 때  N > M인 경우 
  적어도 하나의 둥지에는 두 마리 이상의 비둘기가 들어가게 된다는 원리
'''


def cal(x, y):
    count = 0

    for i in range(4):
        if x[i] != y[i]:
            count += 1

    return count


for _ in range(int(input())):
    N = int(input())
    mbti = list(input().split())
    answer = 12

    # mbti는 총 16개이므로, 33명이 된다면 적어도 하나의 유형은 3개 이상 중복됨
    if N > 32:
        print(0)
        continue

    combs = combinations(mbti, 3)

    for comb in combs:
        d = cal(comb[0], comb[1]) + cal(comb[1], comb[2]) + cal(comb[0], comb[2])
        answer = min(answer, d)

    print(answer)