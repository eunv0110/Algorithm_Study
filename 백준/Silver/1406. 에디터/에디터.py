import sys
#문자열 입력
left_stack=list(sys.stdin.readline().strip())
right_stack=[]

#명령어 개수
m=int(input())
for _ in range(m):
  command=sys.stdin.readline().split()
  if command[0]=='P':
    left_stack.append(command[1])
  elif command[0]=='L' and left_stack:
    right_stack.append(left_stack.pop())
  elif command[0]=='D' and right_stack:
    left_stack.append(right_stack.pop())
  elif command[0]=='B' and left_stack:
    if len(left_stack)!=0:
      left_stack.pop()


print(''.join(left_stack + list(reversed(right_stack))))