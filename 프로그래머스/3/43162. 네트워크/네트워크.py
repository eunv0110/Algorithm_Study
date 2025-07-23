from collections import deque

def solution(n, computers):
    visited=[False]*n
    answer = 0
    
    for i in range(n):
        if not visited[i]:
            bfs(i,visited,computers)
            answer+=1
    return answer

def bfs(v,visited,computers):
    
    queue=deque([v])
    visited[v]=True #방문처리
    
    while queue:
        x=queue.popleft()
        
        for i in range(len(computers[x])):
            if computers[x][i]==1 and not visited[i]:
                visited[i]=True
                queue.append(i)