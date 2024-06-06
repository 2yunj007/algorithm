def solution(s):
    answer = ''
    
    words = list(s.split(" "))
    
    for i in range(len(words)):
        new_word = ""
        if words[i]:
            if words[i][0].isalpha():
                new_word = words[i].title()
            else:
                new_word = words[i].lower()
        
            words[i] = new_word
    
    answer = " ".join(words)
    
    return answer