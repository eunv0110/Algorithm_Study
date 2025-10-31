from collections import deque
def solution(n, computers):
    visited=[False]*(n)
    answer = 0

    for i in range(n):
        if not visited[i]:
            bfs(i,visited,computers)
            answer+=1
    return answer

def bfs(node,visited,graph):
    queue=deque([node])
    visited[node]=True #방문처리
    
    while queue: # 큐가 빌때까지 반복
        n=queue.popleft()
        
        for nx in range(len(graph)):
            if not visited[nx] and graph[n][nx]==1:
                queue.append(nx)
                visited[nx]=True
                