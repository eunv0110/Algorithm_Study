from itertools import permutations

def solution(k, dungeons):
    cases=list(permutations(dungeons,len(dungeons)))
    answer=[]
    for case in cases:
        #원래 피로도로 리셋
        need=k
        count=0
        
        for c in case:
            if need>=c[0]:
                need-=c[1]
                count+=1
            else:
                break
        answer.append(count)
                
    return max(answer)
                
        
        
