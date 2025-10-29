n=int(input())
l=list(map(int,input().split(' ')))
l.sort(reverse=True)
answer=0
for i in range(1,n):
  answer+=(l[0]+l[i])
print(answer)
