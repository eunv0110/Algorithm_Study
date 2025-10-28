n,k=map(int,input().split(' '))
coins=[int(input()) for _ in range(n)]
coins.reverse()
answer=0
for coin in coins:
  count=0
  if k==0:
    break
  if k>=coin:
    count=k//coin
    answer+=count
    k=k-count*coin
print(answer)