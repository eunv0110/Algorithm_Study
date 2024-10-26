from collections import deque

# n, m 입력받기
n, m = map(int, input().split())

# 미로 정보 입력받기
graph = []
for _ in range(n):
    graph.append(list(map(int, input().strip())))

# 이동 방향 설정 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 미로 범위를 벗어나면 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            
            # 벽이면 무시
            if graph[nx][ny] == 0:
                continue

            # 처음 방문하는 경우에만 거리 업데이트
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

    # 목표 지점의 최단 거리 반환
    return graph[n - 1][m - 1]

# bfs 시작
print(bfs(0, 0))
