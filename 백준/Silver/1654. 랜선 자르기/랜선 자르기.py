k,n=map(int,input().split(' '))
nums=[]
for _ in range(k):
  nums.append(int(input()))
answer=0
start=1
end=max(nums)

def find_answer(start,end,answer):
  
  if start>end:
    return answer

  total=0

  mid=(start+end)//2

  for num in nums:
    total+=num//mid
  
  if n>total:
    return find_answer(start,mid-1,answer)
  else:
    answer=mid
    return find_answer(mid+1,end,answer)

answer=find_answer(start,end,answer)
print(answer)