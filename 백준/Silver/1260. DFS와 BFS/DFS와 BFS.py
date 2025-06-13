from collections import deque

#정점의 개수 n, 간선의 개수 m, 탐색 시작 번호 v

n,m,v=map(int,input().split())

graph=[[] for _ in range(n+1)]
visited1=[False]*(n+1)
visited2=[False]*(n+1)

for _ in range(m):
  n1,n2=map(int,input().split())
  graph[n1].append(n2)
  graph[n2].append(n1)


for i in range(1, n+1):
  graph[i].sort()

def dfs(v):

  visited2[v]=True
  print(v,end=" ")

  for i in graph[v]:
    if not visited2[i]:
      dfs(i)

def bfs(v):

  queue=deque([v])
  visited1[v]=True

  while queue:

    v=queue.popleft()
    print(v,end=" ")

    for i in graph[v]:
      if not visited1[i]:
        queue.append(i)
        visited1[i]=True
dfs(v)
print("")
bfs(v)
