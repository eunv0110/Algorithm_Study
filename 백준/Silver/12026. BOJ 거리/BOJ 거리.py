n=int(input())
s=input().strip()
INF=float('inf')
dp=[INF]*n
dp[0]=0 #시작점

for i in range(n):
  for j in range(i+1,n):
    if s[i]=='B' and s[j]=='O':
      dp[j]=min(dp[j],dp[i]+(j-i)**2)
    elif s[i]=='O' and s[j]=='J':
      dp[j]=min(dp[j],dp[i]+(j-i)**2)
    elif s[i]=='J' and s[j]=='B':
      dp[j]=min(dp[j],dp[i]+(j-i)**2)

if dp[-1]==INF:
  print(-1)
else:
  print(dp[-1])
