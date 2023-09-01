s = input()
b = input()
stack = []

for i in range(len(s)):
    stack.append(s[i])
    if len(stack) >= len(b):
        if ''.join(stack[len(stack)-len(b):]) == b:
            for j in range(len(b)):
                stack.pop()

if stack:
    print(''.join(stack))
else:
    print('FRULA')