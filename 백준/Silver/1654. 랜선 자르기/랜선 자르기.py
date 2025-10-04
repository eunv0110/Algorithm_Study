k,n=map(int,input().split(' '))
nums=[]
for _ in range(k):
  nums.append(int(input()))
start=1
end=max(nums)
result=0
while start<=end:

  mid=(start+end)//2
  total=0

  for num in nums:
    total+=(num//mid)
  
  
  if total>=n:
    result=mid
    start=mid+1
  
  else:
    end=mid-1

print(result)