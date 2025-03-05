#수열의 길이 입력받음
n=int(input())
stack=[]
for _ in range(n):
  num=int(input())
  stack.append(num)
#+,- 저장
answer=[]
result=[]
now=1
for num in stack:
  while num>=now:
    answer.append(now)
    now+=1
    result.append("+")
  
  if answer[-1]==num:
    answer.pop()
    result.append('-')
  else:
    print("NO")
    exit(0)

print("\n".join(result))