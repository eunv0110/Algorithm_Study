from collections import deque
n,m,v=map(int,input().split())
graph=[[] for _ in range(n+1)]
visited=[False]*(n+1)
visited2=[False]*(n+1)

for _ in range(m):
  a,b=map(int,input().split())
  graph[a].append(b)
  graph[b].append(a)

# 정점 번호가 작은 순서대로 탐색하도록 정렬
for i in range(1, n+1):
    graph[i].sort()

def bfs(v):
  #큐 생성
  queue=deque()
  #현재 방문중인 노드 꺼내기
  queue.append(v)
  visited[v]=True
  
  while queue:
    v=queue.popleft() #큐에서 첫번째 노드 꺼내기
    print(v,end=' ')
    for i in graph[v]:
      if not visited[i]:
        visited[i]=True
        queue.append(i)

def dfs(v):
  visited2[v]=True
  print(v,end=' ')
  for i in graph[v]:
    if not visited2[i]:
      dfs(i)
      
dfs(v)
print()
bfs(v)
