n=int(input())
nums=list(map(int,input().split(' ')))
max_num=int(input())
start=0
end=max(nums)
answer=0

while end>=start:

  mid=(start+end)//2
  total=0

  for num in nums:
    if num>mid:
      total+=mid
    else:
      total+=num
  
  if max_num>=total:
    start=mid+1
    answer=mid
  else:
    end=mid-1
print(answer)
