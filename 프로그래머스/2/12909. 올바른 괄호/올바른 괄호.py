def solution(s):
    answer=[]
    
    for i in s:
        if i =='(':
            answer.append(i)
        elif i==')':
            if answer:
                answer.pop()
            else:
                return False
    if answer:
        return False
    else:
        return True