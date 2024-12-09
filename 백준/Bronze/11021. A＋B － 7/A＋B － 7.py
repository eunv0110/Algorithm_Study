T=int(input())
answers=[]
for i in range(T):
  a,b=map(int,input().split())
  answers.append(a+b)

for i,answer in enumerate(answers):
  print(f"Case #{i+1}:",answer)