from collections import deque

n,m=map(int,input().split(' '))
graph=[]
dx=[-1,1,0,0,-1,1,-1,1]
dy=[0,0,-1,1,1,1,-1,-1]
dist=[[-1]*m for _ in range(n)]

for _ in range(n):
  graph.append(list(map(int,input().split(' '))))

queue=deque()

for y in range(n):
  for x in range(m):
    if graph[y][x]==1:
      queue.append((y,x))
      dist[y][x]=0


while queue:
  y,x=queue.popleft()

  for i in range(8):
    nx=dx[i]+x
    ny=dy[i]+y

    if 0<=nx<m and 0<=ny<n and dist[ny][nx]==-1:
        queue.append((ny,nx))
        dist[ny][nx]=dist[y][x]+1

print(max(max(row) for row in dist))