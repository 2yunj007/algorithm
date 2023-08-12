N = int(input())
student = list(map(int, input().split()))
stack = ['']*N  # 한 명씩 설 수 있는 공간
top = -1
pas = 1     # 현재 들어갈 순서
rst = 'Nice'

i = 0
while i != N:
    # 스택의 top에 있으면 스택에서 삭제
    if stack[top] == pas:
        pas += 1
        top -= 1
    # i번째 학생이 지금 들어갈 순서라면 pass
    elif student[i] == pas:
        pas += 1
        i += 1
    # i번째 학생이 지금 들어갈 순서가 아니면서 스택에도 없으면 삽입
    else:
        top += 1
        stack[top] = student[i]
        i += 1

# 스택에 학생이 남아 있을 경우 수행
for i in range(top+1):
    # top에 있는 학생이 지금 들어갈 순서라면 pass
    if stack[top] == pas:
        top -= 1
        pas += 1
    # 아니라면 Sad
    else:
        rst = 'Sad'

print(rst)