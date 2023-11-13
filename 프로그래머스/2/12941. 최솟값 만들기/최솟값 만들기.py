def solution(A,B):
    answer = 0
    
    A.sort()
    B.sort()
    N = len(A)
    
    for i in range(N):
        answer += A[i] * B[N-i-1]            

    return answer