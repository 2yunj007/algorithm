# 덧셈 연산하는 부분에 괄호 치기
# 숫자를 스택에 넣으면서
# '+' 만나면 두 수를 pop하여 덧셈 연산하고 다시 push
# 마지막에 모든 수 뺄셈 연산

ex = input()
stack = []
opr = ['']
rst = 0

for i in ex:
    if not i.isdigit():
        opr.append(i)

ex = ex.replace('+', ' ').replace('-', ' ')
num = list(map(int, ex.split()))

for i in range(len(num)):
    stack.append(num[i])
    if opr[i] == '+':
        num1 = stack.pop()
        num2 = stack.pop()
        stack.append(num1 + num2)

rst = stack[0]
for i in range(1, len(stack)):
    rst -= stack[i]

print(rst)