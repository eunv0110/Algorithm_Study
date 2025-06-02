from collections import deque

def solution(maps):
    #방향
    answer=bfs(0,0,maps)
    
    if answer==1:
        if len(maps)!=1 and len(maps[0])!=1:
            return -1
     
    return answer

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(y,x,maps):
    
    queue=deque([(y,x)])
    
    while queue:
        y,x=queue.popleft()
        
        for i in range(4):
            nx=dx[i]+x
            ny=dy[i]+y
            
            #먼저 범위 안에 있는지 체크
            if 0<=nx<len(maps[0]) and 0<=ny<len(maps):
                #방문한적이 있는지 체크
                if maps[ny][nx]==1:
                    maps[ny][nx]=maps[y][x]+1
                    queue.append((ny,nx))
                    
    return maps[len(maps)-1][len(maps[0])-1]
    
    