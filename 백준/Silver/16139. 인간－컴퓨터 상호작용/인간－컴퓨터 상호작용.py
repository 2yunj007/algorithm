import sys
input = sys.stdin.readline

S = input().strip() # 문자열
N = len(S)  # 문자열 길이
q = int(input())    # 질문 수
# 각 알파벳에 해당하는 인덱스를 저장할 딕셔너리
alpha = {
            'a': [], 'b': [], 'c': [], 'd': [], 'e': [],
            'f': [], 'g': [], 'h': [], 'i': [], 'j': [],
            'k': [], 'l': [], 'm': [], 'n': [], 'o': [],
            'p': [], 'q': [], 'r': [], 's': [], 't': [],
            'u': [], 'v': [], 'w': [], 'x': [], 'y': [], 'z': []
        }

for i in range(N):
    alpha[S[i]].append(i)
# alpha = {'a': [6, 10], 'b': [], 'c': [], 'd': [], 'e': [1, 7], ...}

for _ in range(q):
    a, *s = input().split()
    l, r = map(int, s)

    # 저장된 인덱스를 순회하면서 범위 안에 들어오면 카운트
    cnt = 0
    for i in alpha[a]:
        if l <= i <= r:
            cnt += 1

    print(cnt)