from collections import deque
def solution(maps):
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    
    def bfs(x,y):
        queue=deque([(x,y)])
        maps[x][y]=1
        
        while queue:
            x,y=queue.popleft()
            
            for i in range(4):
                nx=dx[i]+x
                ny=dy[i]+y
                
                if nx<0 or nx>=len(maps) or ny<0 or ny>=len(maps[0]) or maps[nx][ny]==0:
                    continue
                if maps[nx][ny]==1:
                    #상하좌우 업데이트
                    maps[nx][ny]=maps[x][y]+1
                    queue.append((nx,ny))
        return maps[len(maps)-1][len(maps[0])-1]
    
    #시작점에서 실행
    answer=bfs(0,0)
    if answer>1:
        return answer
    else:
        return -1
