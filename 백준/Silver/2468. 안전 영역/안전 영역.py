from collections import deque

n=int(input())
graph=[]

dx=[-1,1,0,0]
dy=[0,0,-1,1]

for _ in range(n):
  info=list(map(int,input().split()))
  graph.append(info)

def bfs(x,y,visited,rain_h):
  queue=deque([(x,y)])
  visited[x][y]=True #방문처리

  while queue:
    x,y=queue.popleft()

    for i in range(4):
      nx=dx[i]+x
      ny=dy[i]+y

      if 0<=nx<n and 0<=ny<n and not visited[nx][ny] and graph[nx][ny]>rain_h:
        visited[nx][ny]=True
        queue.append((nx,ny))


answer=0
for rain_h in range(0,101):
  visited=[[False]*n for _ in range(n)]
  safe_area=0

  for i in range(n):
    for j in range(n):
      if not visited[i][j] and graph[i][j]>rain_h:
        bfs(i,j,visited,rain_h)
        safe_area+=1
  
  answer=max(answer,safe_area)


print(answer)
