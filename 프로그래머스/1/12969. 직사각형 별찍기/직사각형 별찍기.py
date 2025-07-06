a, b = map(int, input().strip().split(' '))
stars=list('*'*a for _ in range(b))
print('\n'.join(stars))