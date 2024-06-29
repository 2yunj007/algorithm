import sys
input = sys.stdin.readline


p, m = map(int, input().split())
rooms = []

for _ in range(p):
    level, nickname = input().split()
    level = int(level)

    # 방이 없으면 생성
    if len(rooms) == 0:
        rooms.append({
            "start": level - 10,
            "end": level + 10,
            "player": [(level, nickname)]
        })
    else:
        is_join = False

        # 입장 가능한 방 찾기
        for room in rooms:
            if len(room["player"]) < m and room["start"] <= level <= room["end"]:
                is_join = True
                room["player"].append((level, nickname))
                break

        # 입장 가능한 방이 없었다면 생성
        if not is_join:
            rooms.append({
                "start": level - 10,
                "end": level + 10,
                "player": [(level, nickname)]
            })

for room in rooms:
    room["player"].sort(key=lambda x: x[1])

    if len(room["player"]) == m:
        print("Started!")
    else:
        print("Waiting!")

    for player in room["player"]:
        print(*player)