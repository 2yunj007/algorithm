import sys
input = sys.stdin.readline
#sys.stdin = open('input.txt')

K = int(input())
stack = [0]*K
top = -1

for i in range(K):
    N = int(input())
    if N != 0:
        top += 1
        stack[top] = N
    else:
        top -= 1

if top == -1:
    print(0)
else:
    rst = 0
    for i in range(top+1):
        rst += stack[i]
    print(rst)