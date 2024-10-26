N = int(input())
graph = []
result = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 단지 정보 입력 받기
for _ in range(N):
    graph.append(list(map(int, input().strip())))

# dfs 함수 정의
def dfs(x, y):
    global count
    graph[x][y] = 0  # 현재 집 방문 처리
    count += 1  # 현재 위치의 집 개수 증가

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # 범위를 벗어나거나 집이 없는 경우 무시
        if nx < 0 or nx >= N or ny < 0 or ny >= N or graph[nx][ny] == 0:
            continue

        # 연결된 집 탐색
        dfs(nx, ny)

for i in range(N):
    for j in range(N):
        # 새로운 단지를 발견한 경우
        if graph[i][j] == 1:
            count = 0  # 각 단지의 집 개수를 세기 위해 초기화
            dfs(i, j)
            result.append(count)  # 단지 내 집의 수 저장

# 단지 수와 각 단지의 집 수를 오름차순으로 출력
print(len(result))
for count in sorted(result):
    print(count)
