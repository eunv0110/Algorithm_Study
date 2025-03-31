import sys
#회의 수 입력받기
n=int(sys.stdin.readline().strip())

times=[]

for _ in range(n):
  start,end=map(int,sys.stdin.readline().split())
  times.append([start,end])

times.sort(key=lambda x:(x[1],x[0]))

count=0
last_time=0
for start,end in times:
  if start>=last_time:
    count+=1
    last_time=end

print(count)