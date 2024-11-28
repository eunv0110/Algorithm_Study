from collections import deque

def solution(maps):
    # 방향 설정
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    def bfs(x, y):
        # 큐 선언
        queue = deque()
        queue.append((x, y))
        
        while queue:
            x, y = queue.popleft()  # 현재 노드 좌표
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                # 맵의 범위를 벗어나면 무시하기
                if nx < 0 or nx >= len(maps) or ny < 0 or ny >= len(maps[0]):
                    continue
                # 벽이면 무시하기
                if maps[nx][ny] == 0:
                    continue
                # 처음 지나가는 길이라면 상하좌우 확인하기
                if maps[nx][ny] == 1:
                    maps[nx][ny] = maps[x][y] + 1
                    queue.append((nx, ny))
        
        # 상대 팀 진영까지의 거리 반환
        return maps[len(maps) - 1][len(maps[0]) - 1]

    # 시작점에서 BFS 실행
    count = bfs(0, 0)
    # 도달할 수 없으면 -1 반환
    return count if count > 1 else -1
