from collections import deque
n,m=map(int,input().split(' '))
graph=[list(map(int,input().split(' '))) for _ in range(n)]
dist=[[-1]*m for _ in range(n)]
dx=[-1,1,0,0,-1,-1,1,1]
dy=[0,0,-1,1,1,-1,-1,1]
queue=deque()
#상어가 있는 위치
for y in range(n):
  for x in range(m):
    if graph[y][x]==1:
      queue.append((y,x))
      dist[y][x]=0

def bfs():

  while queue:
    
    y,x=queue.popleft()

    for i in range(8):
      nx=x+dx[i]
      ny=y+dy[i]

      if 0<=nx<m and 0<=ny<n:
        if graph[ny][nx]==0 and dist[ny][nx]==-1:
          queue.append((ny,nx))
          dist[ny][nx]=dist[y][x]+1

bfs()

answer=0

for row in dist:
  answer=max(answer,max(row))
print(answer)
  