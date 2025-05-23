from collections import deque
import sys
sys.setrecursionlimit(10**6)

#n-세로, m - 가로, k,음식물 쓰레기 개수
n,m,k=map(int,input().split())

graph=[[0]*m for _ in range(n)]

dx=[-1,1,0,0]
dy=[0,0,-1,1]

for _ in range(k):
  r,c=map(int,input().split())
  graph[r-1][c-1]=1 #음식물 심기

def dfs(y,x):
  graph[y][x]=0 #방문처리
  count=1

  for i in range(4):
    nx=dx[i]+x
    ny=dy[i]+y

    if 0<=nx<m and 0<=ny<n and graph[ny][nx]==1:
      count+=dfs(ny,nx)
  return count

answer=0
for i in range(n):
  for j in range(m):
    if graph[i][j]==1:
      answer=max(answer,dfs(i,j))

print(answer)
