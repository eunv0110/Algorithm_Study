from collections import deque

def solution(n, computers):
    
    visited=[False]*n
    answer=0
    for i in range(n):
        if not visited[i]:
            bfs(i,computers,visited)
            answer+=1
            
        
    
    return answer

def bfs(node,computers,visited):
    
    queue=deque([node])
    
    while queue:
        
        node=queue.popleft()
        
        for i in range(len(computers)):
            if computers[i][node]==1 and not visited[i]:
                queue.append(i)
                visited[i]=True
    