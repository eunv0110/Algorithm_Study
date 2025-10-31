n,m=map(int,input().split(' '))
results=[]
visited=[False]*(n+1)

def recur(start):

  if len(results)==m:
    print(' '.join(map(str,results)))
    return
  
  for i in range(start,n+1):
    if not visited[i]:
      results.append(i)
      recur(i+1)
      results.pop()
recur(1)