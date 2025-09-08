from collections import deque

n,m=map(int,input().split(' '))
graph=[]
dx=[-1,1,0,0]
dy=[0,0,-1,1]

for _ in range(n):
  graph.append(list(map(int,list(input()))))

def bfs(y,x):
  queue=deque([(y,x)])

  while queue:
    y,x=queue.popleft()

    for i in range(4):
      nx=x+dx[i]
      ny=y+dy[i]

      if 0<=nx<m and 0<=ny<n:
        if graph[ny][nx]==1:
          queue.append((ny,nx))
          graph[ny][nx]=graph[y][x]+1
  return graph[-1][-1]

print(bfs(0,0))