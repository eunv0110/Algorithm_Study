T=int(input())
for _ in range(T):
  s=input().split(' ')
  answer=[]
  for i in s:
    answer.append(i[::-1])
  print(' '.join(answer))