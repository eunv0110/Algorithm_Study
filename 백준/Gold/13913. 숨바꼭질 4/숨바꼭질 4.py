from collections import deque

n,k=map(int,input().split(' '))
MAX_NUM=100001
visited=[False]*MAX_NUM
prev=[-1]*MAX_NUM


def bfs(n):

  queue=deque([n])
  visited[n]=True
  dist=[0]*MAX_NUM

  while queue:

    x=queue.popleft()

    if x==k:
      return dist[x]

    for nx in (x+1,x-1,2*x):
      if 0<=nx<MAX_NUM and not visited[nx]:
        queue.append(nx)
        visited[nx]=True
        dist[nx]=dist[x]+1
        prev[nx]=x #어디서 왔는지 기록

path=[]
print(bfs(n))
cur = k

while cur!=-1:
  path.append(cur)
  cur=prev[cur]
path.reverse()
print(' '.join(map(str,path)))     