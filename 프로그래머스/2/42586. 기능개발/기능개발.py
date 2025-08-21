def solution(progresses, speeds):
    answer=[]
    while progresses:
        count=0
        for idx in range(len(progresses)):
            progresses[idx]+=speeds[idx]
        while progresses and progresses[0]>=100:
            progresses.pop(0)
            speeds.pop(0) 
            count+=1
        if count>0:
            answer.append(count)
    return answer
        
