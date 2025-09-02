from collections import deque

#정점의 개수,간선의 개수, 시작노드
n,m,v=map(int,input().split())

graph=[[] for _ in range(n+1)] #노드가 1부터 시작하기 때문에
visited=[False]*(n+1)
visited2=[False]*(n+1)

for _ in range(m):
  a,b=map(int,input().split())
  graph[a].append(b)
  graph[b].append(a)

#그래프 정렬
for i in range(1,n+1):
  graph[i].sort()

def dfs(v):
  visited[v]=True #방문처리
  print(v,end=' ')
  for i in graph[v]:
    if not visited[i]:
      dfs(i)

def bfs(v):

  queue=deque([v])
  visited2[v]=True #방문처리

  while queue:
    x=queue.popleft()
    print(x,end=' ')

    for i in graph[x]:
      if not visited2[i]:
        queue.append(i)
        visited2[i]=True
dfs(v)
print('')
bfs(v)