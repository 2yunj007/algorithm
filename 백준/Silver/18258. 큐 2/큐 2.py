import sys
N = int(input())
input = sys.stdin.readline
queue = []
bot = 0     # 큐의 시작 인덱스

for i in range(N):
    comd = input().split()
    # case 1
    if comd[0] == 'push':
        queue.append(comd[1])
    # case 2
    elif comd[0] == 'pop':
        if len(queue) > bot:  # 큐의 길이 > bot이면 원소가 남아 있다는 것
            print(queue[bot])
            bot += 1
        else:
            print(-1)
    # case 3
    elif comd[0] == 'size':
        print(len(queue)-bot)
        # queue[bot:] -> 시간 초과
        # 슬라이싱 s[a:b] 시간 복잡도: O(b-a)
        # len 시간 복잡도: O(1)
    # case 4
    elif comd[0] == 'empty':
        if len(queue) > bot:
            print(0)
        else:
            print(1)
    # case 5
    elif comd[0] == 'front':
        if len(queue) > bot:
            print(queue[bot])
        else:
            print(-1)
    # case 6
    elif comd[0] == 'back':
        if len(queue) > bot:
            print(queue[-1])
        else:
            print(-1)
