# n : 나무의 수, m: 상근이가 원하는 나무의 수
n,m=map(int,input().split(' '))
trees=list(map(int,input().split(' ')))
start=0
end=max(trees)
answer=0
def recur(start,end,answer):
  
  height=0
  if start>end:
    return answer
  
  mid=(start+end)//2

  for tree in trees:
    if tree>mid:
      height+=tree-mid
  
  #자른 양이 부족 : 더 낮게 잘라야함
  if m>height:
    return recur(start,mid-1,answer)
    
  #자른 양이 충분 : 더 높게 잘라보기
  else:
    answer=mid
    return recur(mid+1,end,mid)

print(recur(start,end,answer))
