from collections import deque

def solution(n, computers):
    visited=[False]*n
    answer = 0
    for i in range(n):
        if not visited[i]:
            answer+=1
            bfs(i,computers,visited)
    return answer

def bfs(node,computers,visited):
    
    queue=deque([node])
    visited[node]=True #방문처리
    
    while queue:
        n=queue.popleft()
        
        for nx in range(len(computers)):
            if computers[n][nx]==1 and not visited[nx]:
                queue.append(nx)
                visited[nx]=True