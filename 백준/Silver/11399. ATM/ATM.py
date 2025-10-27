n=int(input())
p=list(reversed(sorted(map(int,input().split(' ')))))
time=0
total=0
for _ in range(n):
  time+=p.pop()
  total+=time

print(total)