from collections import deque

#세로 n, 가로 m, 쓰레기 개수 k
n,m,k=map(int,input().split())
graph=[[0]*m for _ in range(n)]
for _ in range(k):
  r,c=map(int,input().split(' '))
  graph[r-1][c-1]=1

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(y,x):
  
  queue=deque([(y,x)])
  graph[y][x]=0
  count=1

  while queue:
    y,x=queue.popleft()

    for i in range(4):
      nx=dx[i]+x
      ny=dy[i]+y

      if 0<=nx<m and 0<=ny<n and graph[ny][nx]==1:
        queue.append((ny,nx))
        graph[ny][nx]=0
        count+=1
  return count
answer=0
for y in range(n):
  for x in range(m):
    if graph[y][x]==1:
      answer=max(answer,bfs(y,x))

print(answer)