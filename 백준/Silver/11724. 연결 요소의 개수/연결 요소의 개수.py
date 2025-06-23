from collections import deque
import sys

input=sys.stdin.readline
n,m=map(int,input().split())

visited=[False]*(n+1)

graph=[[] for _ in range(n+1)]

#그래프 연결하기
for _ in range(m):
  a,b=map(int,input().split())
  graph[a].append(b)
  graph[b].append(a)

def bfs(v):
  
  queue=deque([v])
  visited[v]=True #방문처리

  while queue:
    x=queue.popleft()

    for i in graph[x]:
      if not visited[i]:
        queue.append(i)
        visited[i]=True

count=0

for i in range(1,n+1):
  if not visited[i]:
    bfs(i)
    count+=1

print(count)
