from collections import deque

dx=[-1,1,0,0,-1,1,-1,1]
dy=[0,0,-1,1,1,1,-1,-1]

def bfs(y,x):

  graph[y][x]=0 #방문처리

  queue=deque([(y,x)])

  while queue:

    y,x=queue.popleft()

    for i in range(8):

      nx=dx[i]+x
      ny=dy[i]+y

      if 0<=nx<w and 0<=ny<h and graph[ny][nx]==1:
        queue.append((ny,nx))
        graph[ny][nx]=0 #방문처리

while True:

  w,h=map(int,input().split())
  graph=[]

  if w==0 and h==0:
    break

  for _ in range(h):
    graph.append(list(map(int,input().split())))

  count=0

  for y in range(h):
    for x in range(w):
      if graph[y][x]==1:
        bfs(y,x)
        count+=1
  print(count)
