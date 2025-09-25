from collections import deque

n=int(input())
graph=[]
visited=[[False]*n for _ in range(n)]
visited2=[[False]*n for _ in range(n)]

for _ in range(n):
  graph.append(list(input()))

graph2=[row[:] for row in graph]

for y in range(n):
  for x in range(n):
    if graph2[y][x]=='G':
      graph2[y][x]='R'

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(y,x,color,graph,visited):

  queue=deque([(y,x)])
  visited[y][x]=True #방문처리

  while queue:

    y,x=queue.popleft()

    for i in range(4):
      nx=dx[i]+x
      ny=dy[i]+y

      if 0<=nx<n and 0<=ny<n and not visited[ny][nx]:
        if graph[ny][nx]==color:
          queue.append((ny,nx))
          visited[ny][nx]=True

count=0
c_count=0

for y in range(n):
  for x in range(n):
    if not visited[y][x]:
      bfs(y,x,graph[y][x],graph,visited)
      count+=1


for y in range(n):
  for x in range(n):
    if not visited2[y][x]:
      bfs(y,x,graph2[y][x],graph2,visited2)
      c_count+=1
print(count,c_count)


