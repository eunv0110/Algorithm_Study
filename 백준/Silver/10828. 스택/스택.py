import sys
n = int(sys.stdin.readline())

stack = []
for _ in range(n):
    command = sys.stdin.readline().split()

    if command[0] == 'push':
        stack.append(command[1])  # push할 때 command[1]에 있는 값을 추가

    elif command[0] == 'pop':
        if stack:
            print(stack.pop())
        else:
            print(-1)  # 스택이 비어있으면 -1 출력

    elif command[0] == 'size':
        print(len(stack))

    elif command[0] == 'empty':
        print(1 if not stack else 0)  # 삼항연산자로 처리

    elif command[0] == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)  # 스택이 비어있으면 -1 출력
