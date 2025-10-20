from bisect import bisect_left
n=int(input())
nums=list(map(int,input().split(' ')))
answer=[]

for num in nums:

  idx=bisect_left(answer,num)

  if idx==len(answer):
    answer.append(num)
  else:
    answer[idx]=num
  
print(len(answer))