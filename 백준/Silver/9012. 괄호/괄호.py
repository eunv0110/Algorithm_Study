# 괄호
T=int(input())

for _ in range(T):
  stack=[]
  parentheses=list(input())

  for p in parentheses:
    if p=='(' :
      stack.append('(')
    elif p==')':
      if stack:
        stack.pop()
      else:
        print("NO")
        break
  else:
    if stack:
      print("NO")
    else:
      print("YES")