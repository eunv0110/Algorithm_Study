from itertools import permutations
def solution(k, dungeons):
    
    answer=[]
    
    dungeons_list=list(permutations(dungeons,len(dungeons)))
    
    
    for dungeons in dungeons_list:
        
        count=0
        my_level=k

        for min_level, loss_level in dungeons:
            
            if my_level>=min_level:
                count+=1
                my_level=my_level-loss_level
        answer.append(count)
    return max(answer)