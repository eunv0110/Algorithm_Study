import sys
input = sys.stdin.readline

n = int(input())
T = [0] * (n + 1)
P = [0] * (n + 1)
dp = [0] * (n + 2)  # ✅ n+2로 수정

for i in range(1, n + 1):
    T[i], P[i] = map(int, input().split())

max_profit = 0
for i in range(1, n + 1):
    max_profit = max(max_profit, dp[i])  # 지금 시점까지 가능한 최대 이익
    if i + T[i] <= n + 1:
        dp[i + T[i]] = max(dp[i + T[i]], max_profit + P[i])

print(max(max_profit, max(dp)))  # 혹은 그냥 max(dp)로 출력 가능
