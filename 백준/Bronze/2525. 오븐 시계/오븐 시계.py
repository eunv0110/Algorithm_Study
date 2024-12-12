a,b=map(int,input().split())
c=int(input())

time=b+c
while time>=60:
  time=time-60
  a+=1
  if a>=24:
    a=a-24

print(a, time)