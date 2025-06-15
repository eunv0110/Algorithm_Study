from collections import deque

def solution(maps):
    answer = bfs(0,0,maps)
    
    if answer==1:
        return -1
    
    return bfs(0,0,maps)

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(y,x,maps):
    
    queue=deque([(y,x)])
    
    while queue:
        
        y,x=queue.popleft()
        
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            
            if 0<=nx<len(maps[0]) and 0<=ny<len(maps):
                if maps[ny][nx]==1:
                    queue.append((ny,nx))
                    maps[ny][nx]=maps[y][x]+1
    return maps[-1][-1]
    