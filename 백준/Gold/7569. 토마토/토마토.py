from collections import deque

m,n,h=map(int,input().split(' '))

graph=[]

dx=[-1,1,0,0,0,0]
dy=[0,0,-1,1,0,0]
dz=[0,0,0,0,-1,1]

for z in range(h):
  layers=[]
  for y in range(n):
    layer=list(map(int,input().split(' ')))
    layers.append(layer)
  graph.append(layers)


def bfs():

  queue=deque()

  for z in range(h):
    for y in range(n):
      for x in range(m):
        if graph[z][y][x]==1:
          queue.append((z,y,x))
  
  while queue:
    z,y,x=queue.popleft()

    for i in range(6):
      nx=x+dx[i]
      ny=y+dy[i]
      nz=z+dz[i]

      if 0<=nx<m and 0<=ny<n and 0<=nz<h:
        if graph[nz][ny][nx]==0:
          graph[nz][ny][nx]=graph[z][y][x]+1
          queue.append((nz,ny,nx))

bfs()

answer=0
for z in range(h):
  for y in range(n):
    for x in range(m):
      if graph[z][y][x] == 0: 
        print(-1)
        exit()
      answer = max(answer, graph[z][y][x])
print(answer-1)    