from collections import deque

#m은 가로, n은 세로
m,n=map(int,input().split())

graph=[]

for _ in range(n):
  graph.append(list(map(int,input().split())))

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs():
  
  queue=deque()

  for y in range(n):
    for x in range(m):
      if graph[y][x]==1:
        queue.append((y,x))

  while queue:

    y,x=queue.popleft()

    for i in range(4):
      nx=x+dx[i]
      ny=y+dy[i]

      if 0<=nx<m and 0<=ny<n:
        if graph[ny][nx]==0:
          graph[ny][nx]=graph[y][x]+1
          queue.append((ny,nx))


bfs()

answer=0

for row in graph:
  if 0 in row:
    print(-1)
    exit()
  else:
    answer=max(answer,max(row))


print(answer-1)
