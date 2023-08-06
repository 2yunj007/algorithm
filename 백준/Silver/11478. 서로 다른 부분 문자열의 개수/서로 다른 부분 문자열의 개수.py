S = input()
rst = set()

for i in range(len(S)):
    for j in range(1, len(S)+1):
        rst.add(S[i:i+j])

print(len(rst))