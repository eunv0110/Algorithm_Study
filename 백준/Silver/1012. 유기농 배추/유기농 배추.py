from collections import deque
#테스트 케이스 T
T=int(input())

dx=[-1,1,0,0]
dy=[0,0,-1,1]


def bfs(y,x):

  queue=deque([(y,x)])

  graph[y][x]=0 #방문처리

  while queue:

    y,x=queue.popleft()

    for i in range(4):
      nx=x+dx[i]
      ny=y+dy[i]

      if 0<=nx<m and 0<=ny<n:
        if graph[ny][nx]==1:

          graph[ny][nx]=0 #방문처리

          queue.append((ny,nx))

for _ in range(T):
  graph=[]
  count=0
  #가로길이 m,세로길이 n,배추개수 k
  m,n,k=map(int,input().split())

  #그래프 생성
  graph=[[0]*m for _ in range(n)]

  for _ in range(k):
    x,y=map(int,input().split())
    graph[y][x]=1 #배추심기
  
  for y in range(n):
    for x in range(m):
      if graph[y][x]==1:
        bfs(y,x)
        count+=1
  
  print(count)
