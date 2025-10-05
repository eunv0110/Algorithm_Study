from collections import deque
n=int(input())
graph=[]
dx=[-1,1,0,0]
dy=[0,0,-1,1]

for _ in range(n):
  graph.append(list(input()))

color_graph=[row[:] for row in graph]

for y in range(n):
  for x in range(n):
    if color_graph[y][x]=='G':
      color_graph[y][x]='R'


def bfs(y,x,color,graph,visited):

  queue=deque([(y,x)])
  visited[y][x]=True

  while queue:
    y,x=queue.popleft()

    for i in range(4):
      nx=x+dx[i]
      ny=y+dy[i]

      if 0<=nx<n and 0<=ny<n:
        if graph[ny][nx]==color:
          if not visited[ny][nx]:
            queue.append((ny,nx))
            visited[ny][nx]=True

def count_area(graph):
  visited=[[False]*n for _ in range(n)]
  count=0
  for y in range(n):
    for x in range(n):
      if not visited[y][x]:
        bfs(y,x,graph[y][x],graph,visited)
        count+=1
  return count

print(count_area(graph),count_area(color_graph))
