from collections import deque
import sys

N = int(sys.stdin.readline())
dq = deque()

for i in range(N):
    cmd = sys.stdin.readline().split()
    # case 1
    if cmd[0] == '1':
        dq.appendleft(cmd[1])
    # case 2
    elif cmd[0] == '2':
        dq.append(cmd[1])
    # case 3
    elif cmd[0] == '3':
        if len(dq) != 0:
            print(dq.popleft())
        else:
            print(-1)
    # case 4
    elif cmd[0] == '4':
        if len(dq) != 0:
            print(dq.pop())
        else:
            print(-1)
    # case 5
    elif cmd[0] == '5':
        print(len(dq))
    # case 6
    elif cmd[0] == '6':
        if len(dq) != 0:
            print(0)
        else:
            print(1)
    # case 7
    elif cmd[0] == '7':
        if len(dq) != 0:
            print(dq[0])
        else:
            print(-1)
    # case 8
    elif cmd[0] == '8':
        if len(dq) != 0:
            print(dq[-1])
        else:
            print(-1)
