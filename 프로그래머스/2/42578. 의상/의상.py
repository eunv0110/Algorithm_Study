from collections import defaultdict
def solution(clothes):
    
    clothes_dict=defaultdict(list)
    
    for cloth,kind in clothes:
        clothes_dict[kind].append(cloth)
    
    answer=1
    
    for kind in clothes_dict:
        answer*=(len(clothes_dict[kind])+1)
    
    return answer-1