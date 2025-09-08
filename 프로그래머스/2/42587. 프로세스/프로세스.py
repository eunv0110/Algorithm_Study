from collections import deque
def solution(priorities, location):
    queue=deque()
    sorted_priorities = deque(sorted(priorities,reverse=True))
    count=0
    for idx,priority in enumerate(priorities):
        queue.append((idx,priority))
    print(queue)
    while queue:
        idx,importance=queue.popleft()
        
        if importance>=sorted_priorities[0]:
            count+=1
            sorted_priorities.popleft()
            if idx==location:
                return count
        else:
            queue.append((idx,importance))