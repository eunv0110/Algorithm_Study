n=int(input())
arrays=list(sorted(map(int,input().split(' '))))
m=int(input())
nums=list(map(int,input().split(' ')))

def search(start,end,target):
  if start>end:
    return 0

  mid=(start+end)//2

  if arrays[mid]==target:
    return 1
  
  elif arrays[mid]>target:
    return search(start,mid-1,target)
  
  else:
    return search(mid+1,end,target)
  

for num in nums:
  print(search(0,n-1,num))