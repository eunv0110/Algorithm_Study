from collections import deque


dx=[-1,1,0,0,0,0]
dy=[0,0,-1,1,0,0]
dz=[0,0,0,0,-1,1]


def bfs(z,y,x,visited):

  queue=deque([(z,y,x,0)])
  visited[z][y][x]=True #방문처리

  while queue:
    
    z,y,x,count=queue.popleft()

    if graph[z][y][x]=='E':
      print(f"Escaped in {count} minute(s).")
      return

    for i in range(6):
      nz=z+dz[i]
      ny=y+dy[i]
      nx=x+dx[i]

      if 0<=nx<C and 0<=ny<R and 0<=nz<L:
        if graph[nz][ny][nx] in ('.','E'):
          if not visited[nz][ny][nx]:
            queue.append((nz,ny,nx,count+1))
            visited[nz][ny][nx]=True

  print("Trapped!")

while True:

  L,R,C=map(int,input().split(' '))

  if L==0 and R==0 and C==0:
    break

  graph=[]

  visited=[[[False]*C for _ in range(R)]for _ in range(L)]

  for z in range(L):
    layer =[]
    for y in range(R):
      layer.append(list(input()))
    graph.append(layer)
    input()

  for z in range(L):
      for y in range(R):
          for x in range(C):
              if graph[z][y][x] == 'S':
                  bfs(z, y, x,visited)

