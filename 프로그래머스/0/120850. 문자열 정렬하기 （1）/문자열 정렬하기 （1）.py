def solution(my_string):
    alphbet='abcdefghijklmnopqrstuvwxyz'
    answer=[]
    for i in range(len(my_string)):
        if alphbet.find(my_string[i])==-1:
            answer.append(int(my_string[i]))
            
        
    return sorted(answer)