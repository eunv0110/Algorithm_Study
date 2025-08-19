from collections import deque

#n 가로크기, m 세로크기
n,m=map(int,input().split())

graph=[]
visited=[[False]*n for _ in range(m)]
dx=[-1,1,0,0]
dy=[0,0,-1,1]

for _ in range(m):
  graph.append(list(input()))

def bfs(y,x,color):

  queue=deque([(y,x)])
  visited[y][x]=True
  count=1

  while queue:
    y,x=queue.popleft()

    for idx in range(4):
      nx=dx[idx]+x
      ny=dy[idx]+y

      if 0<=nx<n and 0<=ny<m:
        if graph[ny][nx]==color and not visited[ny][nx]:
          queue.append((ny,nx))
          visited[ny][nx]=True
          count+=1

  return count

w_sum=0
b_sum=0

for y in range(m):
  for x in range(n):
    if graph[y][x]=='W' and not visited[y][x]:
      w_sum+=bfs(y,x,'W')**2
    elif graph[y][x]=='B' and not visited[y][x]:
      b_sum+=bfs(y,x,'B')**2

print(w_sum,b_sum)