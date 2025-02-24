def solution(s):
    answer = []
    
    for char in s:
        if char=='(':
            answer.append(char)
        else:
            if not answer:
                return False
            answer.pop()
    return not answer
        
    
