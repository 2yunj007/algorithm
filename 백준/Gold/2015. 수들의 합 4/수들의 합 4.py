import sys
input = sys.stdin.readline

n, k = map(int, input().split())
input_data = list(map(int, input().split()))

# 20억이므로 리스트 x
sum_dict = {0: 1}

sum_ = 0
answer = 0

for i in input_data:
    sum_ += i

    # 즉 누적합 - k 값이 이전에 나왔으면
    if sum_ - k in sum_dict.keys():
        answer += sum_dict[sum_ - k]

    # 누적합 딕셔너리 갱신
    sum_dict[sum_] = sum_dict.get(sum_, 0) + 1

print(answer)