#나무의 수 : n, 상근이가 집으로 가져가려고 하는 나무의 길이 m
n,m=map(int,input().split(' '))
trees=list(map(int,input().split(' ')))
start=0
end=max(trees)
result = 0

while start<=end:
  mid=(start+end)//2
  
  total=0
   
  for tree in trees:
    if tree>mid:
      total+=tree-mid
  if total>=m:
    result=mid
    start=mid+1
  else:
    end=mid-1

print(result)