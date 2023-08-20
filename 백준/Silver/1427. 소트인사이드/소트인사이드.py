import sys
input = sys.stdin.readline
arr = sorted(map(int, input().strip()), reverse=True)
for i in arr:
    print(i, end='')