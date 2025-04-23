#백준 9094번
import sys

T=int(sys.stdin.readline().strip())

for _ in range(T):
  n,m=map(int,sys.stdin.readline().split())
  count=0
  for b in range(2,n):
    for a in range(1,b):
      if ((a**2)+(b**2)+m)%(a*b)==0:
        count+=1
  print(count)
