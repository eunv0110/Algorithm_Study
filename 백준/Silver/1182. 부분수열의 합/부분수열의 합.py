n,s=map(int,input().split(' '))
nums=list(map(int,input().split(' ')))
results=[]
count=0
def recur(start):
  global count
  if results and sum(results)==s:
    count+=1

  for i in range(start,n):
    results.append(nums[i])
    recur(i+1)
    results.pop()

recur(0)

print(count)