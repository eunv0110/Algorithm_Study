from collections import deque
def solution(n, wires):
    answer=n
    for i in range(len(wires)):
        graph = [[] for _ in range(n+1)]
        visited=[False]*(n+1) 
        for idx,(v1,v2) in enumerate(wires):
            if idx!=i:
                graph[v1].append(v2)
                graph[v2].append(v1)       
        for node in range(1,n+1):
            if not visited[node]:
                count=bfs(graph,node,visited)
                break
        diff=abs(count-(n-count))
        answer=min(answer,diff)
        if answer==0:
            break
    return answer
        
def bfs(graph,start,visited):
    queue=deque([start])
    visited[start]=True
    count=1
    
    while queue:
        
        node=queue.popleft()
        
        for next_node in graph[node]:
            if not visited[next_node]:
                queue.append(next_node)
                visited[next_node]=True
                count+=1
    return count
    
    
    