#최소 이동 거리 -> dfs
from collections import deque

dx=[-1,1,0,0]
dy=[0,0,-1,1]

n,m=map(int,input().split())
graph=[]

for _ in range(n):
  info=list(map(int,input()))
  graph.append(info)

def bfs(x,y):
  queue=deque([(x,y)])
  while queue:
    x,y=queue.popleft()

    for i in range(4):
      nx=dx[i]+x
      ny=dy[i]+y

      if nx<0 or nx>=n or ny<0 or ny>=m or graph[nx][ny]==0:
        continue
      if graph[nx][ny]==1:
        graph[nx][ny]=graph[x][y]+1
        queue.append((nx,ny))
  return graph[n-1][m-1]
    
print(bfs(0,0))
