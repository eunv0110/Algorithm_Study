from collections import deque

n,k=map(int,input().split(' '))
MAX_NUM=100001
dist=[-1]*MAX_NUM
ways=[0]*MAX_NUM

def bfs(n):

  dist[n]=0
  ways[n]=1
  queue=deque([n])

  while queue:

    x=queue.popleft()

    for nx in (x-1,x+1,2*x):
      if 0<=nx<MAX_NUM:
        #한번도 방문하지 않은 경우
        if dist[nx]==-1:
          ways[nx]=ways[x]
          dist[nx]=dist[x]+1
          queue.append(nx)
        #방문한적이 있는 경우
        elif dist[nx]==dist[x]+1:
          ways[nx]+=ways[x]

bfs(n)
print(dist[k])
print(ways[k])      
      
        
