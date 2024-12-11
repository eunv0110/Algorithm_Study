from collections import deque

n, k = map(int, input().split())  # 수빈이와 동생의 위치를 입력받는다

MAX = 100000
ways = [0] * (MAX + 1)        # 경우의 수를 기록
visited = [0] * (MAX + 1)     # 최단 시간을 기록

def bfs(n):
    queue = deque([n])        # 큐 선언
    ways[n] = 1               # 시작점의 경우의 수는 1
    visited[n] = 1            # 시작점 방문 (0초로 시작)

    while queue:
        x = queue.popleft()

        for next in (x - 1, x + 1, 2 * x):
            # 범위를 벗어나지 않고
            if 0 <= next <= MAX:
                # 방문한 적이 없으면
                if visited[next] == 0:
                    visited[next] = visited[x] + 1  # 방문 시간 업데이트
                    ways[next] = ways[x]            # 경우의 수 기록
                    queue.append(next)

                # 같은 최단 시간에 도달한 경우
                elif visited[next] == visited[x] + 1:
                    ways[next] += ways[x]

# 출발지와 도착지가 같은 경우
if n == k:
    print(0)
    print(1)
else:
    bfs(n)
    print(visited[k] - 1)  # 최단 시간 (초기값이 1이므로 1을 빼줌)
    print(ways[k])         # 최단 시간에 도달하는 경우의 수
