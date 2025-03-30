import sys

n,k=map(int,sys.stdin.readline().split())
coins=[]
result=0
i=0

for _ in range(n):
  coin=int(sys.stdin.readline().strip())
  if k>=coin:
    coins.append(coin)
coins.reverse()

while i<len(coins):
  result+=k//coins[i]
  k=k%coins[i]
  i+=1

print(result)