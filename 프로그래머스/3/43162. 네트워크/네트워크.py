from collections import deque

def solution(n, computers):
    answer = 0
    visited=[False]*n
    for i in range(n):
        if not visited[i]:
            bfs(i,visited,computers)
            answer+=1
    return answer

def bfs(node,visited,computers):
    
    queue=deque([node])
    visited[node]=True
    
    while queue:
        x=queue.popleft()
        
        for nx in range(len(computers)):
            if computers[x][nx]==1 and not visited[nx]:
                queue.append(nx)
                visited[nx]=True

