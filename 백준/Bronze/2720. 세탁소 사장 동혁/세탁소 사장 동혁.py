T = int(input())
for _ in range(T):
    chan = int(input())
    lst = []    # 쿼터(0.25), 다임(0.1), 니켈(0.05), 페니(0.01)
    for i in [25, 10, 5, 1]:
        cnt = 0
        while chan - i >= 0:
            chan -= i
            cnt += 1
        lst.append(cnt)
    print(*lst)