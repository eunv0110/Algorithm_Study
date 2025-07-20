def solution(participant, completion):
    p_dict={}
    p_sum=0
    for p in participant:
        p_dict[hash(p)]=p
        p_sum+=hash(p)
    
    for c in completion:
        p_sum-=hash(c)
    return p_dict[p_sum]
        