n,m=map(int,input().split(' '))
trees=list(map(int,input().split(' ')))
start=0
end=max(trees)
answer=0
def recur(start,end,answer):
  if start>end:
    return answer

  mid=(start+end)//2

  total=0
  for tree in trees:
    total+=max(0,tree-mid)
  
  if total>=m:
    return recur(mid+1,end,mid)
  else:
    return recur(start,mid-1,answer)
print(recur(start,end,answer))


