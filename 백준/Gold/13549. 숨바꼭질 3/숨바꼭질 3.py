from collections import deque

n,k=map(int,input().split(' '))
MAX_NUM=100001
visited=[False]*(MAX_NUM+1)

def bfs(v):
  queue=deque([(v,0)])
  visited[v]=True

  while queue:

    x,count=queue.popleft()

    if x==k:
      return count
    nx=x*2
    if 0<=nx<MAX_NUM and not visited[nx]:
      queue.append((nx,count))
      visited[nx]=True
    
    for nx in (x-1,x+1):
      if 0<=nx<MAX_NUM and not visited[nx]:
        queue.append((nx,count+1))
        visited[nx]=True

print(bfs(n))