import sys
input = sys.stdin.readline


def find_set(x):
    if parent[x] != x:
        parent[x] = find_set(parent[x])
    return parent[x]


def union(x, y):
    # 이미 같은 집합인 지 체크
    x = find_set(x)
    y = find_set(y)

    # 같은 집합이라면 (대표자가 같으면) 사이클 발생
    if x == y:
        # return False
        # 사이클이 발생해도 다른 트리가 존재할 수 있음
        # 사이클이 발생한 케이스를 저장
        cycle.append(x)
        return

    # 다른 집합이라면 같은 대표자로 수정
    if x < y:
        parent[y] = x
    else:
        parent[x] = y
    # return True


tc = 0
while True:
    N, M = map(int, input().split())

    # 테스트 케이스 종료
    if N == 0 and M == 0:
        break

    tc += 1  # 테스트 케이스 증가
    parent = [i for i in range(N + 1)]
    cycle = []

    for _ in range(M):
        a, b = map(int, input().split())
        union(a, b)

    # 부모 갱신
    for i in range(1, N + 1):
        find_set(i)

    # 사이클이 발생한 해당 노드의 부모를 저장
    cycle_occurs = set()
    for i in cycle:
        cycle_occurs.add(parent[i])

    tree_cnt = 0
    for i in range(1, N + 1):
        # 사이클이 발생한 그룹에 포함된다면 (혹은 이미 카운트했다면) pass
        if parent[i] in cycle_occurs:
            continue
        tree_cnt += 1
        cycle_occurs.add(parent[i])

    if tree_cnt == 1:
        print(f"Case {tc}: There is one tree.")
    elif tree_cnt > 1:
        print(f"Case {tc}: A forest of {tree_cnt} trees.")
    else:
        print(f'Case {tc}: No trees.')