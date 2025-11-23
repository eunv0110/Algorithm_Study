n,m=map(int,input().split(' '))
trees=list(map(int,input().split(' ')))
answer=0
start=0
end=max(trees)

def recur(start,end,answer):

  if start>end:
    return answer
  
  mid=(start+end)//2
  total=0

  for tree in trees:
    if tree>mid:
      total+=tree-mid
  
  #만약에 target보다 total의 값이 작으면
  #자르는 나무의 키를 줄여야한다

  if m>total:
    return recur(start,mid-1,answer)
  #만약에 target이 total 값보다 크거나 같으면
  #자르는 나무의 키를 늘려야한다
  else:
    return recur(mid+1,end,mid)
print(recur(start,end,answer))
