def solution(progresses, speeds):
    answer=[]
    while progresses:
        for idx in range(len(progresses)):
            progresses[idx]+=speeds[idx]
        count=0  
        if progresses[0]>=100:
            while progresses and progresses[0]>=100:
                progresses.pop(0)
                speeds.pop(0)
                count+=1
        if count>0:
            answer.append(count)
    return answer
                    
        
        
    answer = []
    return answer