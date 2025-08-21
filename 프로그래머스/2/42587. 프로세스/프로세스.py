from collections import deque
def solution(priorities, location):
    queue=deque()
    sorted_priorities=sorted(priorities,reverse=True)
    for idx,priority in enumerate(priorities):
        queue.append((idx,priority))
        
    answer=0
    
    while queue:
        idx,priority=queue.popleft()
        if queue and priority < sorted_priorities[answer]:
            queue.append((idx,priority))
        else:
            answer+=1
            if idx==location:
                return answer
        