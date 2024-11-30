from collections import deque

# 가로, 세로, 높이 입력받기
m, n, h = map(int, input().split())

# 방향 설정
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

# 입력받기
boxes = []
queue = deque()

for z in range(h):
    box = []
    for y in range(n):
        row = list(map(int, input().split()))
        for x in range(m):
            if row[x] == 1:  # 익은 토마토 위치를 큐에 추가
                queue.append((z, y, x))
        box.append(row)
    boxes.append(box)

# BFS 함수
def bfs():
    while queue:
        z, y, x = queue.popleft()
        for i in range(6):
            nz, ny, nx = z + dz[i], y + dy[i], x + dx[i]
            # 범위를 벗어나면 무시
            if nz < 0 or nz >= h or ny < 0 or ny >= n or nx < 0 or nx >= m:
                continue
            # 익지 않은 토마토(0)만 전파
            if boxes[nz][ny][nx] == 0:
                boxes[nz][ny][nx] = boxes[z][y][x] + 1
                queue.append((nz, ny, nx))

# BFS 실행
bfs()

# 결과 계산
answer = 0
for z in range(h):
    for y in range(n):
        for x in range(m):
            if boxes[z][y][x] == 0:  # 익지 않은 토마토가 남아 있다면
                print(-1)
                exit()
            answer = max(answer, boxes[z][y][x])

# 출력 (1을 빼서 일수 계산)
print(answer - 1)
