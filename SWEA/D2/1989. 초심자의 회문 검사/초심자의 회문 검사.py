T = int(input())
for tc in range(1, T+1):

    word = input()
    check = 0
    # 뒤집은 문자열과 일치하면 회문이므로 check = 1
    if word == word[::-1]:
        check = 1

    print(f'#{tc} {check}')