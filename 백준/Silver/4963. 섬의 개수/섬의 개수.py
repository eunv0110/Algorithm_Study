from collections import deque

dx=[-1,1,0,0,1,-1,-1,1]
dy=[0,0,-1,1,1,-1,1,-1]

def bfs(y,x,graph):
  
  queue=deque([(y,x)])

  graph[y][x]=0 #방문처리

  while queue:
    y,x=queue.popleft()

    for i in range(8):
      nx=dx[i]+x
      ny=dy[i]+y

      if 0<=nx<w and 0<=ny<h:
        if graph[ny][nx]==1:
          graph[ny][nx]=0
          queue.append((ny,nx))

while True:
  graph=[]
  answer=0

  w,h=map(int,input().split())

  if w==0 and h==0:
    break

  for _ in range(h):
    graph.append(list(map(int,input().split())))
  
  for y in range(h):
    for x in range(w):
      if graph[y][x]==1:
        bfs(y,x,graph)
        answer+=1
  print(answer)



