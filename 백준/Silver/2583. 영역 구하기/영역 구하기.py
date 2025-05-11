from collections import deque
#m이 가로, n이 세로
m,n,k=map(int,input().split())
graph=[[0]*m for _ in range(n)]

for _ in range(k):
  x1,y1,x2,y2=map(int,input().split())
  for i in range(x1,x2):
    for j in range(y1,y2):
      graph[i][j]=1

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(x,y):
  queue=deque([(x,y)])
  graph[x][y]=1 #방문처리
  count=1

  while queue:
    x,y=queue.popleft()   

    for i in range(4):
      nx=x+dx[i]
      ny=y+dy[i]

      if 0<=nx<n and 0<=ny<m and graph[nx][ny]==0:
        queue.append((nx,ny))
        graph[nx][ny]=1 #방문처리
        count+=1
  return count


results=[]
for i in range(n):
  for j in range(m):
    if graph[i][j]==0:
      results.append(bfs(i,j))

results.sort()
print(len(results))

for result in results:
  print(result)