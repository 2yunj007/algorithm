import sys
input = sys.stdin.readline
N = int(input())
stack = []

for i in range(N):
    comd = input().split()
    # case 1
    if comd[0] == '1':
        stack.append(comd[1])
    # case 2
    elif comd[0] == '2':
        # 스택에 정수가 있으면 맨 위 정수를 빼고 출력
        if stack:
            print(stack.pop())
        # 스택에 정수가 없으면 -1 출력
        else:
            print(-1)
    # case 3
    elif comd[0] == '3':
        print(len(stack))
    # case 4
    elif comd[0] == '4':
        # 스택이 비어 있지 않으면 0 출력
        if stack:
            print(0)
        # 스택이 비어 있으면 1 출력
        else:
            print(1)
    # case 5
    elif comd[0] == '5':
        if stack:
            print(stack[-1])
        else:
            print(-1)