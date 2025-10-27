from collections import deque

n=int(input())
graph=[list(input()) for _ in range(n)]
blind_graph=[row[:] for row in graph]
dx=[-1,1,0,0]
dy=[0,0,-1,1]
#적록색약 그래프 만들기
for y in range(n):
  for x in range(n):
    if blind_graph[y][x]=='G':
      blind_graph[y][x]='R'

def bfs(y,x,color,graph,visited):
  
  visited[y][x]=True
  queue=deque([(y,x)])

  while queue:
    y,x=queue.popleft()

    for i in range(4):
      nx=x+dx[i]
      ny=y+dy[i]

      if 0<=nx<n and 0<=ny<n:
        if not visited[ny][nx] and graph[ny][nx]==color:
          queue.append((ny,nx))
          visited[ny][nx]=True

def count_area(graph):
  count=0
  visited=[[False]*n for _ in range(n)]
  for y in range(n):
    for x in range(n):
      if not visited[y][x]:
        bfs(y,x,graph[y][x],graph,visited)
        count+=1
  return count

print(count_area(graph), count_area(blind_graph))
