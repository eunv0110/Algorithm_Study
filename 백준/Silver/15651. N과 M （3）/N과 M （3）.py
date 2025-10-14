n,m=map(int,input().split(' '))
results=[]
def recur(depth):
  if depth==m:
    print(' '.join(map(str,results)))
    return
  for i in range(1,n+1):
    results.append(i)
    recur(depth+1)
    results.pop()
recur(0)