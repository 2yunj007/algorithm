import sys
input = sys.stdin.readline

_dict = dict()
divisor = 0

while True:
    word = input().rstrip()

    if not word:
        break

    _dict.setdefault(word, 0)
    _dict[word] += 1
    divisor += 1

for word in sorted(_dict.keys()):
    print("%s %.4f" % (word, _dict[word] / divisor * 100))