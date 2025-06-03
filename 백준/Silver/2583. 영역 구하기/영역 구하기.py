from collections import deque

#가로,세로,테스트 개수
m,n,k=map(int,input().split())

#그래프 만들기
graph=[[0]*m for _ in range(n)]


for _ in range(k):
  y1,x1,y2,x2=map(int,input().split())

  for i in range(y1,y2):
    for j in range(x1,x2):
      graph[i][j]=1

dx=[0,0,-1,1]
dy=[-1,1,0,0]

def bfs(y,x):
  count=1
  queue=deque([(y,x)])
  graph[y][x]=1 #방문처리

  while queue:
    y,x=queue.popleft()
    
    for i in range(4):
      nx=x+dx[i]
      ny=y+dy[i]

      if 0<=nx<m and 0<=ny<n:
        if graph[ny][nx]==0:
          graph[ny][nx]=1 #방문처리
          queue.append((ny,nx))
          count+=1
  return count

results=[]

for i in range(n):
  for j in range(m):
    if graph[i][j]==0:
      results.append(bfs(i,j))

results.sort()
print(len(results))           # 영역 개수 먼저 출력

for result in results:
  print(result,end=' ')