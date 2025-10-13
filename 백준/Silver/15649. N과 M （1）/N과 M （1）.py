n,m=map(int,input().split(' '))
visited=[False]*(n+1)
results=[]

def recur(depth):
  if depth==m:
    print(' '.join(map(str,results)))
    return
  
  for i in range(1,n+1):
    if not visited[i]:
      visited[i]=True
      results.append(i)
      recur(depth+1)
      visited[i]=False
      results.pop()
recur(0)