from collections import deque

#가로 n, 세로 m

n,m=map(int,input().split())
visited=[[False]*n for _ in range(m)]
graph=[]

dx=[-1,1,0,0]
dy=[0,0,-1,1]

for _ in range(m):
  graph.append(list(input()))


def bfs(y,x):

  queue=deque([(y,x)])
  visited[y][x]=True
  count=1

  while queue:

    y,x=queue.popleft()

    for i in range(4):
      nx=dx[i]+x
      ny=dy[i]+y

      if 0<=nx<n and 0<=ny<m and not visited[ny][nx]:
        if graph[ny][nx]=='W':
          queue.append((ny,nx))
          visited[ny][nx]=True
          count+=1
  return count


def bfs2(y,x):

  queue=deque([(y,x)])
  visited[y][x]=True

  count=1

  while queue:

    y,x=queue.popleft()

    for i in range(4):
      nx=dx[i]+x
      ny=dy[i]+y

      if 0<=nx<n and 0<=ny<m and not visited[ny][nx]:
        if graph[ny][nx]=='B':
          queue.append((ny,nx))
          visited[ny][nx]=True
          count+=1
  return count


w_count=[]
b_count=[]
for y in range(m):
  for x in range(n):
    if graph[y][x]=='W' and not visited[y][x]:
      w_count.append(bfs(y,x))
    if graph[y][x]=='B' and not visited[y][x]:
      b_count.append(bfs2(y,x))

print(sum(w**2 for w in w_count),sum(b**2 for b in b_count))