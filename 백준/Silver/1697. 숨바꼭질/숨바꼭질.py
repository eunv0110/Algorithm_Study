from collections import deque
import sys

input=sys.stdin.readline
n,k=map(int,input().split(' '))
MAX_NUM=100001
visited=[False]*MAX_NUM

def bfs(n):
  count=0
  queue=deque([(n,count)])
  visited[n]=True

  while queue:

    node,count=queue.popleft()

    if node==k:
      return count
    
    else:
      for i in (node-1,node+1,node*2):
        if 0<=i<MAX_NUM and not visited[i]:
          visited[i]=True
          queue.append((i,count+1))

print(bfs(n))