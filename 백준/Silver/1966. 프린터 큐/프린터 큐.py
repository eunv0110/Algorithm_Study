from collections import deque

def solution(test_cases):
    results = []
    for case in test_cases:
        N, M, priorities = case
        queue = deque([(i, p) for i, p in enumerate(priorities)])
        print_order = 0

        while queue:
            current = queue.popleft()
            if any(current[1] < q[1] for q in queue):
                queue.append(current)
            else:
                print_order += 1
                if current[0] == M:
                    results.append(print_order)
                    break
    return results

# 입력 처리
T = int(input())
test_cases = []
for _ in range(T):
    N, M = map(int, input().split())
    priorities = list(map(int, input().split()))
    test_cases.append((N, M, priorities))

# 결과 출력
results = solution(test_cases)
for result in results:
    print(result)
