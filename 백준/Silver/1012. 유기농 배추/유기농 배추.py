from collections import deque
#테스트 케이스 횟수 입력받기
T=int(input())

#방향 선언
dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(x,y):
  queue=deque() #큐선언
  queue.append((x,y)) #시작노드 추가
  graph[x][y]=0 #방문처리

  while queue:
    x,y=queue.popleft() #노드 꺼내주기

    for i in range(4):
      nx=dx[i]+x
      ny=dy[i]+y

      #범위가 맞지 않는 경우 무시 또는 0이면 무시
      if nx<0 or nx>=M or ny<0 or ny>=N or graph[nx][ny]==0:
        continue
      if graph[nx][ny]==1:
        graph[nx][ny]=0 #방문처리
        queue.append((nx,ny)) 

results=[]

#배추의 정보에 대한 입력받기
for _ in range(T): #테스트 케이스 횟수만큼 반복
  M,N,K=map(int,input().split()) #밭의 가로길이, 세로길이, 위치개수를 다시 입력받음
  graph=[[0] * N for _ in range(M)] #테스트 테이스마다 그래프를 초기화해줘야하니까

  for _ in range(K):
    x,y=map(int,input().split())
    graph[x][y]=1 #배추심기

  count=0
  for i in range(M):
    for j in range(N):
      if graph[i][j]==1:
        bfs(i,j)
        count+=1
  results.append(count)

for result in results:
  print(result)
