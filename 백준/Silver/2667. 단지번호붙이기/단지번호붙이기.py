n=int(input())

graph=[]

for _ in range(n):
    info=list(map(int,input().strip()))
    graph.append(info)

#방향 선언
dx=[-1,1,0,0]
dy=[0,0,-1,1]

def dfs(x,y):
  graph[x][y]=0 #방문처리
  count=1 #개수 하나 세어줌

  for i in range(4):
    nx=dx[i]+x
    ny=dy[i]+y

    #범위를 벗어낫거나 벽일 경우 무시하기
    if nx<0 or nx>=n or ny<0 or ny>=n or graph[nx][ny]==0:
      continue
    if graph[nx][ny]==1:
      count+=dfs(nx,ny)
  return count

results=[]

for i in range(n):
  for j in range(n):
    if graph[i][j]==1:
      results.append(dfs(i,j))

print(len(results))
for result in sorted(results):
  print(result)