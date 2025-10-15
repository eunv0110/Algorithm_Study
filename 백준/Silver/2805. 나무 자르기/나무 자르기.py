n,m=map(int,input().split(' '))
nums=list(map(int,input().split(' ')))
start=0
end=max(nums)
answer=0

def find_height(start,end,answer):
  total=0
  if start>end:
    return answer

  mid=(start+end)//2

  for num in nums:
    total+=max(0,num-mid)

  if total>=m:
    answer=mid
    return find_height(mid+1,end,answer)

  else:
    return find_height(start,mid-1,answer)


answer=find_height(start,end,answer)
print(answer)

