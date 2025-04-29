from collections import deque

f,s,g,u,d=map(int,input().split())
visited=[False]*(f+1)

def bfs(s):
  queue=deque([(s,0)])
  visited[s]=True #방문처리

  while queue:
    x,count=queue.popleft()
    if x==g:
      return count
    for i in (x+u,x-d):
      if 1<=i<=f and not visited[i]:
        visited[i]=True
        queue.append((i,count+1))
  return "use the stairs"
print(bfs(s))