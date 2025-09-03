from collections import deque

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(y,x):
  queue=deque([(y,x)])
  graph[y][x]=0 #방문처리

  while queue:
    y,x=queue.popleft()

    for i in range(4):
      nx=dx[i]+x
      ny=dy[i]+y

      if 0<=nx<m and 0<=ny<n:
        if graph[ny][nx]==1:
          queue.append((ny,nx))
          graph[ny][nx]=0 #방문처리

T=int(input())

for _ in range(T):
  #가로길이 m, 세로길이 n, 배추가 심어져 있는 위치의 개수 k
  m,n,k=map(int,input().split(' '))
  graph=[[0]*m for _ in range(n)]

  for _ in range(k):
    x,y=map(int,input().split(' '))
    graph[y][x]=1

  count=0

  for y in range(n):
    for x in range(m):
      if graph[y][x]==1:
        bfs(y,x)
        count+=1

  print(count)