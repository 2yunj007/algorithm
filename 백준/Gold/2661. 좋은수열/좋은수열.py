def check(S):
    len_ = len(S)
    for i in range(1, len_//2 + 1):
        if S[-i:] == S[-(2*i):-i]:
            return False
    return True


def recur(S):
    if len(S) == N:
        print(S)
        exit()

    for s in '123':
        if check(S + s):
            recur(S + s)


N = int(input())
recur('1')