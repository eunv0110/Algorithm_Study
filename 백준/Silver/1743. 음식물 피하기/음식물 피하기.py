from collections import deque

n,m,k=map(int,input().split())
graph=[[0]*m for _ in range(n)]

for _ in range(k):
  r,c=map(int,input().split())
  graph[r-1][c-1]=1

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(x,y):
  count=1
  queue=deque([(x,y)])
  graph[x][y]=0 #방문처리

  while queue:
    x,y=queue.popleft()
    for i in range(4):
      nx=dx[i]+x
      ny=dy[i]+y

      if nx<0 or nx>=n or ny<0 or ny>=m:
        continue
      if graph[nx][ny]==1:
        count+=1
        queue.append((nx,ny))
        graph[nx][ny]=0 #방문처리
  return count

result=0
for i in range(n):
  for j in range(m):
    if graph[i][j]==1:
      result=max(result,bfs(i,j))

print(result)