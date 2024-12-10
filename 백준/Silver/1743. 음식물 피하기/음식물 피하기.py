from collections import deque

n,m,k=map(int,input().split()) #세로가 N, 가로가 M, 쓰레기의 개수
graph=[[0]*m for _ in range(n)]

dx=[-1,1,0,0]
dy=[0,0,-1,1]

for _ in range(k):
  r,c=map(int,input().split())
  graph[r-1][c-1]=1

def bfs(x,y):
  queue=deque() #큐 생성
  queue.append((x,y))
  graph[x][y]=0 #첫번째 방문처리
  count=1

  while queue: #큐가 빌때까지 반복
    x,y=queue.popleft()

    for i in range(4):
      nx=dx[i]+x
      ny=dy[i]+y

      #범위에 벗어나거나 방문한적이 있거나 음식물쓰레기가 없을때
      if nx<0 or nx>=n or ny<0 or ny>=m or graph[nx][ny]==0:
        continue
      if graph[nx][ny]==1:
        count+=1
        graph[nx][ny]=0 #방문처리
        queue.append((nx,ny))
  return count

results=[]
for i in range(n):
  for j in range(m):
    if graph[i][j]==1:
      results.append((bfs(i,j)))

results.sort(reverse=True)
print(results[0])