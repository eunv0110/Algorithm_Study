from collections import deque
def solution(priorities, location):
    queue=deque()
    
    for idx,priority in enumerate(priorities):
        queue.append((idx,priority))
        
    answer=0
    
    while queue:
        idx,priority=queue.popleft()
        if queue and priority < max(p for i,p in queue):
            queue.append((idx,priority))
        else:
            answer+=1
            if idx==location:
                return answer
        
    return answer