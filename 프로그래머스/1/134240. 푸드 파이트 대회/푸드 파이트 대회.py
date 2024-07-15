def solution(food):
    s=''
    for i in range(1,len(food)):
        n=food[i]//2
        s=s+('{}'.format(i))*n
    s_reverse=s[::-1]
    answer=s+'0'+s_reverse
            
    return answer