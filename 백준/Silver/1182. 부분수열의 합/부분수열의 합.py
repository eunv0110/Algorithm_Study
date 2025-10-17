n,s=map(int,input().split(' '))
nums=list(map(int,input().split(' ')))
answer=0
def recur(idx,total):
  global answer
  if idx==n:
    if total==s:
      answer+=1
    return
  
  recur(idx+1,total+nums[idx])
  recur(idx+1,total)

if s==0:
  answer=answer-1
recur(0,0)
print(answer)