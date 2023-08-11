import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    ps = input().rstrip()   # 괄호 문자열
    N = len(ps) # 문자열 길이
    stack = ['']*N    # 문자열 길이의 크기만큼 stack 생성
    top = -1    # stack의 최상단 값의 idx
    vps = 'YES'  # 괄호 문자열이 올바른지 판단할 변수

    for i in ps:
        if i == '(':    # 열린 괄호를 만나면 top += 1하고 스택에 넣음
            top += 1
            stack[top] = i
        else:   # 닫힌 괄호를 만났는데 스택에 아무것도 없으면 NO
            if top == -1:
                vps = 'NO'
            top -= 1

    if top != -1:   # 문자열을 다 순회했는데 괄호가 남아 있으면 NO
        vps = 'NO'
    print(vps)