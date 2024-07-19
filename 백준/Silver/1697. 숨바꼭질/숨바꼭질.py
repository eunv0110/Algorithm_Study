from collections import deque
import sys

#입력값 받기
n,k=map(int,sys.stdin.readline().split())
max_num=100000
visited=[0]*(max_num+1)

def bfs():
    q=deque()
    #출발점 위치 큐에 삽입
    q.append(n)
    
    while q:
        x=q.popleft()
        #수빈이 위치가 동생 위치와 같다면 반복문 종료
        if x==k:
            print(visited[x])
            break
        #이동할 수 있는 방향
        for i in (x-1,x+1,x*2):
            #주어진 범위내에 있고 아직 방문하지 않았으면
            if 0<=i<=max_num and not visited[i]:
                #이동한 시간 표시
                visited[i]=visited[x]+1
                q.append(i)
bfs()