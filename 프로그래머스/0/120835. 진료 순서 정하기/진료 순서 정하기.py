def solution(emergency):
    sorted_emergency=sorted(emergency,reverse=True)
    
    rank={}
    
    for i in range(len(sorted_emergency)):
        value=sorted_emergency[i]
        rank[value]=i+1
        
    answer = []
    for e in emergency:
        answer.append(rank[e])
    return answer