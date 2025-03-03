import sys

n = int(sys.stdin.readline())

for _ in range(n):
    answer = []
    status = True  # 유효성 체크 변수
    letter = sys.stdin.readline().strip()  # 개행 문자 제거

    for char in letter:
        if char == '(':
            answer.append(char)
        elif char == ')':
            if not answer:  # 스택이 비어 있으면 짝이 맞지 않음
                status = False
                break
            answer.pop()

    if status and not answer:
        print("YES")
    else:
        print("NO")
