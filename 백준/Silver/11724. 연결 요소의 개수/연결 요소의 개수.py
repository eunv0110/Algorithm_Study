from collections import deque
import sys

input=sys.stdin.readline

n,m=map(int,input().strip().split())

graph=[[] for _ in range(n+1)]
visited=[False]*(n+1)

for _ in range(m):
  u,v=map(int,input().split())
  graph[u].append(v)
  graph[v].append(u)

count=0

def bfs(v):
  queue=deque([v])
  visited[v]=True

  while queue:

    v=queue.popleft()

    for i in graph[v]:
      if not visited[i]:
        visited[i]=True
        queue.append(i)

for v in range(1,n+1):
  if not visited[v]:
    bfs(v)
    count+=1

print(count)


