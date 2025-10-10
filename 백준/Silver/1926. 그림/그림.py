from collections import deque

n,m=map(int,input().split(' '))
graph=[]
results=[]

dx=[-1,1,0,0]
dy=[0,0,-1,1]

for _ in range(n):
  graph.append(list(map(int,input().split(' '))))

def bfs(y,x):
  queue=deque([(y,x)])
  count=1
  graph[y][x]=0

  while queue:
    y,x=queue.popleft()

    for i in range(4):
      nx=dx[i]+x
      ny=dy[i]+y

      if 0<=nx<m and 0<=ny<n:
        if graph[ny][nx]==1:
          graph[ny][nx]=0 #방문처리
          queue.append((ny,nx))
          count+=1

  return count

for y in range(n):
  for x in range(m):
    if graph[y][x]==1:
      results.append(bfs(y,x))

if len(results)==0:
  print(0)
  print(0)
else:
  print(len(results))
  print(max(results))