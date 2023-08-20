def merge_sort(arr):
    global cnt, K
    # 길이가 1인 리스트 반환
    # 전부 쪼갠 다음에 두 리스트씩 비교하여 정렬하면서 병합할 거임
    if len(arr) < 2:
        return arr

    mid = (len(arr)+1) // 2

    left_arr = merge_sort(arr[:mid])    # 반으로 잘린 리스트 왼쪽
    right_arr = merge_sort(arr[mid:])   # 반으로 잘린 리스트 오른쪽

    merge_arr = []
    i, j = 0, 0

    while True:
        # 왼쪽 리스트와 오른쪽 리스트의 원소를 앞에서부터 비교하며
        # 정렬하여 새로운 리스트에 넣음
        if left_arr[i] < right_arr[j]:
            merge_arr.append(left_arr[i])
            i += 1
        else:
            merge_arr.append(right_arr[j])
            j += 1

        cnt += 1
        if cnt == K:
            print(merge_arr[-1])
            exit()

        # 하나의 리스트 끝까지 돌았으면 탈출
        if i == len(left_arr) or j == len(right_arr):
            break

    # 남은 원소 마저 넣음
    if i == len(left_arr):  # 왼쪽 리스트를 끝까지 넣었다면
        while j < len(right_arr):  # 오른쪽 리스트의 j부터 끝까지 넣음
            merge_arr.append(right_arr[j])
            j += 1
            cnt += 1
            if cnt == K:
                print(merge_arr[-1])
                exit()

    elif j == len(right_arr):  # 오른쪽 리스트를 끝까지 넣었다면
        while i < len(left_arr):  # 왼쪽 리스트의 i부터 끝까지 넣음
            merge_arr.append(left_arr[i])
            i += 1
            cnt += 1
            if cnt == K:
                print(merge_arr[-1])
                exit()

    return merge_arr


import sys
N, K = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
cnt = 0
merge_sort(arr)
print(-1)   # if cnt == K: exit() 안 걸렸으면 -1 출력