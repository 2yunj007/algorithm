def spin(wheel_num, direction):
    visited.append(wheel_num)

    # 회전시킬 바퀴의 오른쪽, 왼쪽 자석 상태
    right = (cogwheel[wheel_num]['now'] + 2) % 8
    left = (cogwheel[wheel_num]['now'] + 6) % 8

    right_state = cogwheel[wheel_num]['state'][right]
    left_state = cogwheel[wheel_num]['state'][left]

    # 회전
    cogwheel[wheel_num]['now'] -= direction
    if cogwheel[wheel_num]['now'] == 8:
        cogwheel[wheel_num]['now'] = 0
    elif cogwheel[wheel_num]['now'] == -1:
        cogwheel[wheel_num]['now'] = 7

    for i in (-1, 1):
        next_wheel_num = wheel_num + i
        # 범위 벗어났거나 이미 회전 했다면 pass
        if next_wheel_num in (0, T + 1) or next_wheel_num in visited:
            continue

        if i == -1: # 오른쪽 바퀴
            next = (cogwheel[next_wheel_num]['now'] + 2) % 8
            next_state = cogwheel[next_wheel_num]['state'][next]
            now_state = left_state
        else:   # 왼쪽 바퀴
            next = (cogwheel[next_wheel_num]['now'] + 6) % 8
            next_state = cogwheel[next_wheel_num]['state'][next]
            now_state = right_state

        # 극이 다르면 회전
        if next_state != now_state:
            if direction == -1:
                spin(next_wheel_num, 1)
            else:
                spin(next_wheel_num, -1)


T = int(input())

cogwheel = {}
for num in range(1, T + 1):
    cogwheel.setdefault(num, {'state': input(), 'now': 0})

K = int(input())

for _ in range(K):
    wheel_num, direction = map(int, input().split())
    visited = []
    spin(wheel_num, direction)

answer = 0
for i in range(1, T + 1):
    if cogwheel[i]['state'][cogwheel[i]['now']] == '1':
        answer += 1

print(answer)