def f(num):     # 4
    global answer
    if num > b:
        return

    if a <= num <= b:
        answer += 1

    f(num*10 + 4)   # 44
    f(num*10 + 7)   # 47


a, b = map(int, input().split())
answer = 0
f(4)
f(7)
print(answer)