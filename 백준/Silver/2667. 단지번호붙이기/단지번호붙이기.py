from collections import deque

n=int(input())

graph=[]
dx=[-1,1,0,0]
dy=[0,0,-1,1]

for _ in range(n):
  graph.append(list(map(int,input())))

def bfs(y,x):
  
  queue=deque([(y,x)])
  graph[y][x]=0 #방문처리
  count=1

  while queue:

    y,x=queue.popleft()

    for i in range(4):
      nx=dx[i]+x
      ny=dy[i]+y

      if 0<=nx<n and 0<=ny<n and graph[ny][nx]==1:
        queue.append((ny,nx))
        graph[ny][nx]=0
        count+=1
  return count

results=[]

for y in range(n):
  for x in range(n):
    if graph[y][x]==1:
      results.append(bfs(y,x))

print(len(results))
results.sort()

for result in results:
  print(result,end='\n')


  
