from collections import deque

F,S,G,U,D=map(int,input().split())
visited=[0 for _ in range(F+1)]

def bfs(n):
  #큐 선언
  queue=deque([n])
  visited[n]=1

  while queue:
    x=queue.popleft()
    
    if x==G:
      return visited[x]-1
    for i in (x+U,x-D):
      if 1<=i<=F and not visited[i]:
        queue.append(i)
        visited[i]=visited[x]+1
  return "use the stairs"

print(bfs(S))