import sys
input=sys.stdin.readline

n,m=map(int,input().split(' '))
nums=list(map(int,input().split(' ')))
nums.sort()

visited=[False]*n
results=[]

def recur(depth):
  if depth==m:
    print(' '.join(map(str,results)))
    return

  used=set()

  for i in range(n):
    if not visited[i] and nums[i] not in used:
      visited[i]=True #방문처리
      results.append(nums[i])
      used.add(nums[i]) #이번 depth에서 중복 방지
      recur(depth+1)
      visited[i]=False
      results.pop()

recur(0)