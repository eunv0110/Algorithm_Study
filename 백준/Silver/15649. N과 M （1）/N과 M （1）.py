import sys
input=sys.stdin.readline

n,m=map(int,input().split(' '))
visited=[False]*(n+1)
results=[]

def recur(num):

  if num==m:
    print(' '.join(map(str,results)))
    return
  for i in range(1,n+1):
    if not visited[i]:
      visited[i]=True
      results.append(i)
      recur(num+1)
      visited[i]=False
      results.pop()
recur(0)