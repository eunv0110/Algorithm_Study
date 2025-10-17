n,m=map(int,input().split(' '))
results=[]

def recur(start):
  if len(results)==m:
    print(' '.join(map(str,results)))
    return
  
  for i in range(start,n+1):
    results.append(i)
    recur(i)
    results.pop()

recur(1)