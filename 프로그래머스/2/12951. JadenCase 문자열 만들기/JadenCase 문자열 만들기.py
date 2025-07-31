def solution(s):
    
    s=list(s.lower().split(' '))
    answer=[]
    for word in s:
        if word=='':
            answer.append(word)
        else:
            answer.append(word[0].upper()+word[1:])
    return ' '.join(answer)