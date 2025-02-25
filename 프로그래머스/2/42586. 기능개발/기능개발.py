def solution(progresses, speeds):
    answer = []
    
    #progresses가 빌때까지
    while progresses:
        count=0
        
        while progresses and progresses[0]>=100:
            count+=1
            speeds.pop(0)
            progresses.pop(0)
        
        for i in range(len(progresses)):
            progresses[i]=progresses[i]+speeds[i]
        
        if count:
            answer.append(count)
            
            
        
    return answer