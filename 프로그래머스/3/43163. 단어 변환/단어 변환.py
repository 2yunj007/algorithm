from collections import deque

def solution(begin, target, words):
    N = len(words)
    
    visited = [False] * N
    q = deque([(begin, 0)])    
    
    while q:
        tmp, count = q.popleft()
        
        if tmp == target:
            return count
            
        for i in range(N):
            if visited[i]:
                continue
                
            word = words[i]
            is_same = True
            for w in range(len(word)):
                if not is_same and word[w] != tmp[w]:
                    break
                elif word[w] != tmp[w]:
                    is_same = False
            else:
                q.append((word, count + 1))
                visited[i] = True
    return 0
      