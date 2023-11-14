def solution(s):
    answer = True
    
    stack = []
    
    for i in s:
        if i == '(':
            stack.append(i)
        elif i == ')' and stack:
            stack.pop()
        elif i == ')' and not stack:
            return False
    
    if stack:
        return False
    
    return True