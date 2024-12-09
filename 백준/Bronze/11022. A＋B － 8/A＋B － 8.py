T=int(input())
answers=[]
for i in range(T):
    a,b=map(int,input().split())#테스트 케이스마다 입력
    c=a+b
    answers.append([a,b,c])

for idx,answer in enumerate(answers):
  print(f"Case #{idx+1}: {answer[0]} + {answer[1]} = {answer[2]}")