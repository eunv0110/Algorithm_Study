import sys
sys.setrecursionlimit(10**6)#재귀 한도를 크게 설정하여 깊은 재귀 호출을 처리할 수 있도록 설정

T = int(input())#테스트 케이스의 수 입력받음

def dfs(x, y):
    if x < 0 or y < 0 or x >= M or y >= N: #현재 위치가 범위를 벗어나는지 확인
        return False
    if array[x][y] == 1: #현재 위치에 배추가 심어져 있는지 확인
        array[x][y] = 0 # 방문한 위치를 0으로 바꾸어 표시
        #상하좌우 인접한 위치를 재귀적으로 방문
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y+1)
        dfs(x, y-1)
        return True #새로운 연결된 구성 요소를 찾음
    return False #현재 위치에 배추가 없거나 이미 방문한 경우

for i in range(T): #테스트 케이스 반복 처리
    M, N, K = map(int, input().split())# 격자 크기와 배추의 수 입력
    array = [[0] * N for i in range(M)] #격자 0으로 초기화 (배추 없음)

    for i in range(K):#배추의 위치를 읽어서 격자에 표시
        x, y = map(int, input().split())
        array[x][y] = 1 #배추의 위치 표시
    
    # 각 행 순회
    total = 0
    for i in range(M): #각 열 순회
        for j in range(N): #새로운 배추 그룹 찾으면 1증가
            if dfs(i, j) == True:
                total += 1
    print(total)