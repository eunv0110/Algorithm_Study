def solution(s):
    num = '1234567890'
    
    s=s.lower().split(' ')
    answer=[]
    for i in s:
        if i =='':
            answer.append('')
        elif i[0] in num:
            answer.append(i.lower())
        else:
            i=i[0].upper()+i[1:]
            answer.append(i)
    
    return ' '.join(answer)