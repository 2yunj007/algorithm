def pal(S):
    if S == S[::-1]:
        return True
    return False


S = input()
N = len(S)

max_len = 0
for i in range(N-1, -1, -1):
    if pal(S[i:N]):
        max_len = N - i

print(N + N - max_len)