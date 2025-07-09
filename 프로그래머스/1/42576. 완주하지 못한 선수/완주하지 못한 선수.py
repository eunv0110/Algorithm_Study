def solution(participant, completion):
    people = {}
    num=0
    
    for p in participant:
        num+=hash(p)
        people[hash(p)]=p
    
    for c in completion:
        num-=hash(c)
    
    return people[num]
    

