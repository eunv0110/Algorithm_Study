n=int(input())
cards=list(sorted(map(int,input().split(' '))))
m=int(input())
nums=list(map(int,input().split(' ')))

def is_checked(start,end,target,arrays):
  if start>end:
    return 0
  
  mid=(start+end)//2

  if target==arrays[mid]:
    return 1
  elif arrays[mid]>target:
    return is_checked(start,mid-1,target,arrays)
  else:
    return is_checked(mid+1,end,target,arrays)
answer=[]
for num in nums:
  answer.append(is_checked(0,n-1,num,cards))
print(' '.join(map(str,answer)))