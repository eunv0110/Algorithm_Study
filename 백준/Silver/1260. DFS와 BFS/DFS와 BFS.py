from collections import deque

n,m,v=map(int,input().split())
graph=[[]for _ in range(n+1)]
visited=[False]*(n+1)
visited2=[False]*(n+1)

for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(v):
    queue=deque([v])
    visited[v]=True
    
    while queue:
        v=queue.popleft()
        print(v,end=' ')
        for i in sorted(graph[v]):
            if not visited[i]:
                visited[i]=True
                queue.append(i)
def dfs(v):
    visited2[v]=True
    print(v,end=' ')
    for i in sorted(graph[v]):
        if not visited2[i]:
            dfs(i)
            
dfs(v)
print()
bfs(v)