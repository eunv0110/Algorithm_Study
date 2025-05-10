from collections import deque

dx=[-1,1,0,0]
dy=[0,0,-1,1]

#상자의 크기 입력받기
n,m=map(int,input().split())
graph=[]
for _ in range(n):
  graph.append(list(map(int,input().split())))


def bfs(y,x):
  count=1
  queue=deque([(y,x)])
  graph[y][x]=0

  while queue:
    y,x=queue.popleft()

    for i in range(4):
      nx=x+dx[i]
      ny=y+dy[i]

      if 0<=nx<m and 0<=ny<n and graph[ny][nx]==1:
        graph[ny][nx]=0 #방문처리
        queue.append((ny,nx))
        count+=1
  return count

results=[]

for i in range(n):
  for j in range(m):
    if graph[i][j]==1:
      results.append(bfs(i,j))

print(len(results))
if len(results)==0:
  print(0)
else:
  print(max(results))
     