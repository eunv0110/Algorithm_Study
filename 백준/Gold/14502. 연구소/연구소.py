from collections import deque

#세로 n, 가로 m
n,m=map(int,input().split(' '))
graph=[]
answer=[]

for _ in range(n):
  graph.append(list(map(int,input().split(' '))))

empty_location=[]
candidate=[]
results=[]

dx=[-1,1,0,0]
dy=[0,0,-1,1]

#벽을 세울 수 있는 좌표 저장
for y in range(n):
  for x in range(m):
    if graph[y][x]==0:
      empty_location.append((y,x))

#벽을 세울 수 있는 후보지 선정
def recur(start):
  if len(candidate)==3:
    results.append(candidate.copy())
    return

  for i in range(start,len(empty_location)):
    candidate.append(empty_location[i])
    recur(i+1)
    candidate.pop()

recur(0)

def spread_virus(test_graph):
  queue=deque()
  for y in range(n):
    for x in range(m):
      if test_graph[y][x]==2:
        queue.append((y,x))
  while queue:
    y,x=queue.popleft()

    for i in range(4):
      nx=dx[i]+x
      ny=dy[i]+y

      if 0<=nx<m and 0<=ny<n and test_graph[ny][nx]==0:
        queue.append((ny,nx))
        test_graph[ny][nx]=2 #방문처리
  return test_graph

def count_safe(test_graph):
  return sum(row.count(0) for row in test_graph)

for result in results:
  test_graph=[row[:] for row in graph]  
  for y,x in result:
    test_graph[y][x]=1

  answer.append(count_safe(spread_virus(test_graph)))

print(max(answer))