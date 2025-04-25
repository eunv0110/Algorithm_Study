from collections import deque

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(x,y):
  queue=deque([(x,y)])
  graph[y][x]=0 #방문처리

  while queue:
    x,y=queue.popleft() #노드 꺼내주기

    for i in range(4):
      nx=dx[i]+x
      ny=dy[i]+y

      if nx<0 or nx>=m or ny<0 or ny>=n:
        continue
      if graph[ny][nx]==1:
        graph[ny][nx]=0
        queue.append((nx,ny))

T=int(input())
results=[]

for _ in range(T):
  m,n,k=map(int,input().split())
  graph=[[0]*m for _ in range(n)]  
  for _ in range(k):
    x,y=map(int,input().split())
    graph[y][x]=1
  
  count=0

  for i in range(m):
    for j in range(n):
      if graph[j][i]==1:
        bfs(i,j)
        count+=1

  results.append(count)

for result in results:
  print(result)
    