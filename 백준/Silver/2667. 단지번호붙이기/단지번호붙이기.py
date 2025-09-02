n=int(input())
graph=[]

for _ in range(n):
  graph.append(list(map(int,list(input()))))

dx=[-1,1,0,0]
dy=[0,0,-1,1]


def dfs(y,x):
  graph[y][x]=0 #방문처리
  count=1

  for i in range(4):
    nx=x+dx[i]
    ny=y+dy[i]

    if 0<=nx<n and 0<=ny<n:
      if graph[ny][nx]==1:
        count+=dfs(ny,nx)
  return count

results=[]

for y in range(n):
  for x in range(n):
    if graph[y][x]==1:
      results.append(dfs(y,x))
  
results.sort()
print(len(results))
for result in results:
  print(result)