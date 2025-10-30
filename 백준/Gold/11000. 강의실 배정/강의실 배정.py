import sys, heapq
input = sys.stdin.readline

#우선 sort를 하고 할 수 있는 강의실에 다 몰아넣기
n=int(input())
classes=list(tuple(map(int,input().split(' '))) for _ in range(n))
classes.sort(key=lambda x:x[0])
heap=[]
#첫 강의의 종료 시간 집어넣기
heapq.heappush(heap,classes[0][1])

for i in range(1,n):
  start,end=classes[i]
  # 가장 빨리 끝나는 강의실이 지금 수업 시작 전이라면 재사용 가능
  if heap[0]<=start:
    heapq.heappop(heap)
  heapq.heappush(heap,end)

print(len(heap))
