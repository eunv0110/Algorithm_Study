from collections import deque
#f: 총 층, s : 출발점, g : 목적지, 위, 아래
f,s,g,u,d=map(int,input().split(' '))
visited=[False]*(f+1)

def bfs(s):

  queue=deque([(s,0)])
  visited[s]=True

  while queue:

    n,count=queue.popleft()

    if n==g:
      return count

    for nx in (n+u,n-d):
      if 1<=nx<=f:
        if not visited[nx]:
          queue.append((nx,count+1))
          visited[nx]=True

  return "use the stairs"

print(bfs(s))