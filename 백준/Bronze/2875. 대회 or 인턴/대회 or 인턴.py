#2명의 여학생과 1명의 남학생이 한조를 이뤄야함
#인턴학생은 k명이 나가야됨
n,m,k=map(int,input().split(' '))
team=min(n//2,m) #우선 가장 큰 팀 수

remain=n+m-team*3

while remain<k:
  team-=1
  remain+=3

print(team)