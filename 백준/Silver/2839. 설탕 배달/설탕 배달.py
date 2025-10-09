n=int(input())

INF=5001
d=[5001]*(n+1)

if n>=5:
  d[5]=1
if n>=3:
  d[3]=1

for i in range(6,n+1):
  if d[i-3]!=INF or d[i-5]!=INF:
    d[i]=min(d[i-3],d[i-5])+1

if d[n]==INF:
  print(-1)
else:
  print(d[n])
