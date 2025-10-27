n=int(input())
p=list(sorted(map(int,input().split(' '))))
time=0
total=0
for i in p:
  time+=i
  total+=time

print(total)