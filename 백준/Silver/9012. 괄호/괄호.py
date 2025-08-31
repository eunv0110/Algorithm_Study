# 괄호
T=int(input())

for _ in range(T):
  stack=[]
  parentheses=list(input())
  flag=True

  for p in parentheses:
    if p=='(' :
      stack.append('(')
    elif p==')':
      if stack:
        stack.pop()
      else:
        flag=False
        break
  if stack or not flag:
    print("NO")
  else:
    print("YES")