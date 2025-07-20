def solution(s):
    num = '1234567890'
    
    s=s.lower().split(' ')
    answer=[]
    for i in s:
        if i =='':
            answer.append('')
        else:
            i=i[0].upper()+i[1:]
            answer.append(i)
    
    return ' '.join(answer)