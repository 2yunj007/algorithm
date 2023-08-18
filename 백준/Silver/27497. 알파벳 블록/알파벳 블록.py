from collections import deque
import sys

N = int(sys.stdin.readline())
s = deque()
last = []    # 1과 2 중 마지막에 수행된 명령

for _ in range(N):
    bt = sys.stdin.readline().strip()
    # 문자열 맨 뒤에 bt[-1]가 적인 블록 추가
    if bt[0] == '1':
        s.append(bt[-1])
        last.append(1)
    # 문자열 맨 앞에 bt[-1]가 적힌 블록 추가
    elif bt[0] == '2':
        s.appendleft(bt[-1])
        last.append(2)
    # 나중에 추가된 블록 제거
    elif bt[0] == '3':
        try:
            t = last.pop()
            # 맨 뒤에 있는 블록이 나중에 추가된 블록인 경우
            if t == 1:
                s.pop()
            # 맨 앞에 있는 블록이 나중에 추가된 블록인 경우
            elif t == 2:
                s.popleft()
        except IndexError:
            continue

if s:
    print(''.join(s))
else:
    print(0)