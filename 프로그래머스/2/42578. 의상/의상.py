
def solution(clothes):
    
    clothes_dict={}
    
    for cloth,kind in clothes:
        if kind not in clothes_dict:
            clothes_dict[kind]=[cloth]
        else:
            clothes_dict[kind].append(cloth)
        
    result=1

    for kind in clothes_dict:
        result*=(len(clothes_dict[kind])+1)
    

    
    return result-1

