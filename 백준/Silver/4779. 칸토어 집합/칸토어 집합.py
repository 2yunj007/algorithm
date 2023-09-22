def cut(a, n):  # a: 시작점, n: 선의 길이
    # 선의 길이가 1이면 리턴
    if n == 1:
        return

    # 가운데 문자열을 공백으로 변환
    for i in range(a + n//3, a + (n//3)*2):
        result[i] = ' '

    # 왼쪽과 오른쪽에 대해 재귀
    cut(a, n//3)                # 왼쪽
    cut(a + (n//3)*2, n//3)     # 오른쪽


import sys
while True:
    try:
        N = int(sys.stdin.readline())
        result = ['-'] * (3**N)     # 최초 리스트 집합
        cut(0, 3**N)                # 자르기
        print(''.join(result))
    except:
        break