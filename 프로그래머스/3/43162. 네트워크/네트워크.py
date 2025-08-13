from collections import deque

def solution(n, computers):
    visited=[False]*n
    answer = 0

    for i in range(n):
        if not visited[i]:
            bfs(i,computers,visited)
            answer+=1
    return answer


def bfs(node,computers,visited):
    
    queue=deque([node])
    visited[node]=True
    
    while queue:
        
        node=queue.popleft()
        
        for next_node in range(len(computers)):
            if computers[node][next_node]==1 and not visited[next_node]:
                queue.append(next_node)
                visited[next_node]=True
