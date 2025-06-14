from collections import deque
#n이 세로, m이 가로
n,m=map(int,input().split())
#그래프 선언
graph=[]
for _ in range(n):
  graph.append(list(map(int,input())))


dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(y,x):
  queue=deque([(y,x)])

  while queue:
    y,x=queue.popleft()

    for i in range(4):
      nx=dx[i]+x
      ny=dy[i]+y

      if 0<=nx<m and 0<=ny<n and graph[ny][nx]==1:
        graph[ny][nx]=graph[y][x]+1
        queue.append((ny,nx))
  
  return graph[-1][-1]

print(bfs(0,0))