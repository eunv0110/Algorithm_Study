l,c=map(int,input().split(' '))
letters=list(input().split(' '))
letters.sort()
visited=[False]*c
results=[]

def is_valid(password):
  vowel=set('aeiou')
  v_count=0
  m_count=0
  for p in password:
    if p in vowel:
      v_count+=1
    else:
      m_count+=1
  if v_count>=1 and m_count>=2:
    return True
  else:
    return False

def recur(start):
  length=len(results)
  if length==l:
    if is_valid(results):
      print(''.join(results))
    return
  
  for i in range(start,c):
    results.append(letters[i])
    recur(i+1)
    results.pop()
recur(0)


