def solution(s):
    last_seen={}
    result=[]
    
    for index,char in enumerate(s):
        if char in last_seen:
            result.append(index-last_seen[char])
        else:
            result.append(-1)
        last_seen[char]=index
    return result