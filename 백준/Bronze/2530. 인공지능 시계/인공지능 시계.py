a,b,c=map(int,input().split()) #시,분,초
d=int(input())
second=d%60
minute=d//60

#초 계산
c+=second
if c>=60:
  x=c//60
  b=b+x
  c-=60*x

b+=minute
#분 계산
if b>=60:
  y=b//60
  a=a+y
  b-=60*y

#시 계산
a=a%24

print(a ,b ,c)