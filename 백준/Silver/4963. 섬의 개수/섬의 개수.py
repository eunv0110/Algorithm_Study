from collections import deque
#정사각형
#가로,세로,대각선

dx=[-1,1,0,0,-1,-1,1,1]
dy=[0,0,-1,1,-1,1,-1,1]

def bfs(y,x):

  queue=deque([(y,x)])

  #섬은 1, 바다는 0
  graph[y][x]=0 #방문처리

  while queue:
    y,x=queue.popleft()

    for i in range(8):
      nx=x+dx[i]
      ny=y+dy[i]


      if 0<=nx<w and 0<=ny<h and graph[ny][nx]==1:
        queue.append((ny,nx))
        graph[ny][nx]=0 #방문처리

while True:
  
  w,h=map(int,input().split())
  graph=[]
  count=0

  if w==0 and h==0:
    break
  
  for _ in range(h):
    graph.append(list(map(int,input().split())))

  for i in range(h):
    for j in range(w):
      if graph[i][j]==1:
        count+=1
        bfs(i,j)

  print(count)

  

  