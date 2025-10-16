from collections import deque

n,k=map(int,input().split(' '))
MAX_NUM=100001
ways=[0]*MAX_NUM
dist=[-1]*MAX_NUM

def bfs(n):

  queue=deque([n])
  dist[n]=0 #방문처리
  ways[n]=1 #경우의 수 업데이트

  while queue:

    x=queue.popleft()

    for nx in (x-1,x+1,2*x):
      if 0<=nx<MAX_NUM:
        #방문한적이 없다면
        if dist[nx]==-1:
          dist[nx]=dist[x]+1
          ways[nx]=ways[x]
          queue.append(nx)
        
        #최소 길이로 방문한적이 있다면
        elif dist[nx]==dist[x]+1:
          ways[nx]+=ways[x]

bfs(n)
print(dist[k])
print(ways[k])