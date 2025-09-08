from collections import deque
def solution(priorities, location):
    sorted_priorities=deque(sorted(priorities,reverse=True))
    queue=deque()
    answer=0
    
    for idx,p in enumerate(priorities):
        queue.append((idx,p))
        
    while queue:
        idx,p=queue.popleft()
        
        if p>=sorted_priorities[0]:
            answer+=1
            sorted_priorities.popleft()
            if idx==location:
                break
        else:
            queue.append((idx,p))
                
    return answer          
            
