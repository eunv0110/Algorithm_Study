dp=[[0]*4 for _ in range(10001)]
for i in range(4):
  dp[0][i]=1 #초기값 설정

for i in range(1,10001):
  dp[i][1]=1

  if i-2>=0:
    dp[i][2]=dp[i][1]+dp[i-2][2]
  
  else:
    dp[i][2]=dp[i][1]
  
  if i-3>=0:
    dp[i][3]=dp[i][2]+dp[i-3][3]
  else:
    dp[i][3]=dp[i][2]

T = int(input())
for _ in range(T):
    n = int(input())
    print(dp[n][3])
