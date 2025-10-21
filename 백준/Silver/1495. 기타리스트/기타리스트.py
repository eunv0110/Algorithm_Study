N, S, M = map(int, input().split())  # 곡 수, 시작 볼륨, 최대 볼륨
V = list(map(int, input().split()))  # 각 곡마다 조절할 수 있는 볼륨 변화량

#dp[v]= 현재 곡에서 볼륨 v가 가능한지 여부
dp=[False]*(M+1)
dp[S]=True #시작 볼륨은 항상 가능

for i in range(N):
  next_dp=[False]*(M+1) #다음 단계의 볼륨 상태
  for v in range(M+1):
    if dp[v]:
      if v-V[i]>=0:
        next_dp[v-V[i]]=True
      if v+V[i]<=M:
        next_dp[v+V[i]]=True
  dp=next_dp



for v in range(M,-1,-1):
  if dp[v]:
    print(v)
    break

else:
  print(-1)


