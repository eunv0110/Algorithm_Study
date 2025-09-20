n,m=map(int,input().split(' '))
nums=list(map(int,input().split(' ')))
nums.sort()
visited=[False]*n
results=[]

def recur(num):
  if num==m:
    print(' '.join(map(str,results)))
    return
  used=set()
  for i in range(n):
    if not visited[i] and nums[i] not in used:
      visited[i]=True
      results.append(nums[i])
      used.add(nums[i])
      recur(num+1)
      visited[i]=False
      results.pop()

recur(0)