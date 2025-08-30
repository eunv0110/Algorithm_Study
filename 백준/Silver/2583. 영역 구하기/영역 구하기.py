from collections import deque

#m이 세로, n이 가로
m,n,k=map(int,input().split(' '))

graph=[[0]*m for _ in range(n)]

#영역 부분
for _ in range(k):
  y1,x1,y2,x2=map(int,input().split(' '))
  for y in range(y1,y2):
    for x in range(x1,x2):
      graph[y][x]=1

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(y,x):

  queue=deque([(y,x)])
  graph[y][x]=1 #방문처리
  count=1

  while queue:
    y,x=queue.popleft()

    for i in range(4):
      nx=dx[i]+x
      ny=dy[i]+y

      if 0<=nx<m and 0<=ny<n and graph[ny][nx]==0:
        graph[ny][nx]=1
        queue.append((ny,nx))
        count+=1
  return count

results=[]
for y in range(n):
  for x in range(m):
    if graph[y][x]==0:
      results.append(bfs(y,x))
      
results.sort()
print(len(results))
for result in results:
  print(result,end=' ')