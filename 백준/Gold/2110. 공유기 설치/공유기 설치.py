n,c=map(int,input().split(' '))
houses=list(sorted(int(input()) for _ in range(n)))
start=1
end=max(houses)-min(houses)
answer=0

def is_valid(distance):
  location=houses[0]
  count=1

  for i in range(1,n):
    if houses[i]-location>=distance:
      count+=1
      location=houses[i]
  
  if count>=c:
    return True
  return False

while end>=start:

  mid=(start+end)//2

  #mid로 설치가능하면 거리 늘려보기
  if is_valid(mid):
    start=mid+1
    answer=mid
  
  else:
    end=mid-1

print(answer)