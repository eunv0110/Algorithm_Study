from collections import deque

def solution(progresses, speeds):
    
    queue=deque(progresses)
    speeds=deque(speeds)
    answer=[]
    
    #queue 빌때까지
    while queue:
        count=0
        for i in range(len(queue)):
            queue[i]+=speeds[i]
            
        #배포가 완료된 항목들
        #queue가 비고 100% 완료 됐을때
        while queue and queue[0]>=100:
            count+=1
            queue.popleft()
            speeds.popleft()
        
        if count>0:
            answer.append(count)
                
    return answer