n,m=map(int,input().split(' '))
nums=list(sorted(map(int,input().split(' '))))
visited=[False]*n
result=[]

def recur(depth):
  if depth==m:
    print(' '.join(map(str,result)))
    return

  used=set()

  for i in range(n):
    if not visited[i] and not nums[i] in used:
      result.append(nums[i])
      visited[i]=True
      used.add(nums[i])
      recur(depth+1)
      visited[i]=False
      result.pop()

recur(0)
