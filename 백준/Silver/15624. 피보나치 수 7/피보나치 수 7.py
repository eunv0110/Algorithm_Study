n=int(input())
rs=[0,1]

if n==0:
  print(0)
elif n==1:
  print(1)
else:
  for i in range(2,n+1):
    rs.append(((rs[i-1]+rs[i-2])%1000000007))
  print(rs[n])