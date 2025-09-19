n,s=map(int,input().split(' '))
nums=list(map(int,input().split(' ')))
results=[]
count=0
def recur(idx,current_sum):
  global count
  if idx==n:
    if current_sum==s:
      count+=1
    return

  recur(idx+1,current_sum)
  recur(idx+1,current_sum+nums[idx])

recur(0,0)
if s==0:
  print(count-1)
else:
  print(count)