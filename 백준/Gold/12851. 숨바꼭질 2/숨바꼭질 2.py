from collections import deque

n,k=map(int,input().split(' '))
MAX_NUM=100001

ways=[0]*MAX_NUM
dist=[0]*MAX_NUM

def bfs(v):
  queue=deque([v])
  ways[v]=1
  dist[v]=1

  while queue:
    x=queue.popleft()

    for nx in (x-1,x+1,2*x):
      if 0<=nx<MAX_NUM:
        #한번도 방문한적이 없을때
        if dist[nx]==0:
          dist[nx]=dist[x]+1
          ways[nx]=ways[x]
          queue.append(nx)
        #방문한적이 있을때
        elif dist[nx]==dist[x]+1:
          ways[nx]+=ways[x]


if n==k:
  print(0)
  print(1)

else:
  bfs(n)
  print(dist[k]-1)
  print(ways[k])




