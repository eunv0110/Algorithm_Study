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
        print("NO")
        flag=False
        break
  else:
    if stack or not flag:
      print("NO")
    else:
      print("YES")