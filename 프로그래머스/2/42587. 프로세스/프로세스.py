from collections import deque

def solution(priorities, location):
    queue=deque(enumerate(priorities))
    print(queue)
    order=0
    
    while queue:
        #맨 앞 문서에서 꺼내기
        current=queue.popleft()
        #더 높은 우선순위가 있는지 확인
        high=False
        
        for _ ,priority in queue:
            if current[1]<priority:
                high=True
                break
        if high:
            queue.append(current)
        else:
            order+=1
            if current[0]==location:
                return order
    return -1
                
            