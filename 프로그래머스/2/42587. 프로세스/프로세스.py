from collections import deque
def solution(priorities, location):
    sorted_priorities=sorted(priorities,reverse=True)
    
    queue=deque()
    for idx,priority in enumerate(priorities):
        queue.append((idx,priority))
        
    count=0
    while queue:
        idx,p=queue.popleft()
        
        if queue and p<sorted_priorities[count]:
            queue.append((idx,p))
        else:
            count+=1
            if idx==location:
                return count
        
                
                
            