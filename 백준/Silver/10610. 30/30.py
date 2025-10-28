n=list(reversed(sorted(map(int,list(input())))))

if sum(n)%3==0 and n[-1]==0:
  print(''.join(list(map(str,n))))
else:
  print(-1)