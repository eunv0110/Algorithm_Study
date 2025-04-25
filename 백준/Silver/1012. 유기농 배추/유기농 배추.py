import sys
sys.setrecursionlimit(10**6)#재귀 한도 설정
dx=[-1,1,0,0]
dy=[0,0,-1,1]

def dfs(x,y):

  graph[y][x]=0 #방문처리

  for i in range(4):
    nx=x+dx[i]
    ny=y+dy[i]

    if nx<0 or nx>=m or ny<0 or ny>=n:
      continue
    if graph[ny][nx]==1:
      graph[ny][nx]=0
      dfs(nx,ny)

T=int(input())
results=[]

for _ in range(T):
  m,n,k=map(int,input().split())
  graph=[[0]*m for _ in range(n)]  
  for _ in range(k):
    x,y=map(int,input().split())
    graph[y][x]=1
  
  count=0

  for i in range(m):
    for j in range(n):
      if graph[j][i]==1:
        dfs(i,j)
        count+=1

  results.append(count)

for result in results:
  print(result)
    