from collections import deque

#컴퓨터의 수
n=int(input())
graph=[[] for _ in range(n+1)]
visited=[False]*n

#컴퓨터 쌍의 수
m=int(input())

for _ in range(m):
  a,b=map(int,input().split(' '))
  graph[a-1].append(b-1)
  graph[b-1].append(a-1)

def bfs(n):
  visited[n]=True
  queue=deque([n])
  count=0
  while queue:
    n=queue.popleft()

    for nx in graph[n]:
      if not visited[nx]:
        queue.append(nx)
        visited[nx]=True
        count+=1
  return count

print(bfs(0))