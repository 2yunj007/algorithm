while True:
    sent = input()  # 검사할 문장
    if sent == '.': # 온점 하나 입력되면 종료
        break
    N = len(sent)   # 문장 길이
    stack = ['']*N  # 문장 길이 크기의 stack
    top = -1    # stack 최상단 idx
    chk = 'yes' # 응답
    bracket = {'(': ')', '[': ']'}  # 괄호의 짝을 나타냄

    for i in sent:
        # 문자가 열린 괄호라면 스택에 삽입
        if i in bracket.keys():
            top += 1
            stack[top] = i
        # 문자가 닫힌 괄호일 때
        elif i in bracket.values():
            # stack이 비어 있거나 짝이 맞지 않으면 break
            if top == -1 or i != bracket[stack[top]]:
                chk = 'no'
                break
            # 짝이 맞으면 pop 후 계속 순회
            else:
                top -= 1
    # 문장 끝까지 갔는데 스택이 비어 있지 않은 경우
    if top != -1:
        chk = 'no'

    print(chk)