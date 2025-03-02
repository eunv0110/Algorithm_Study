n=int(input())
for _ in range(n):
  answer=[]
  sentence=input().split()
  for i in range(len(sentence)):
    answer.append(''.join(reversed(sentence[i])))  # ✅ 올바르게 문자열 뒤집기

  print(' '.join(answer))