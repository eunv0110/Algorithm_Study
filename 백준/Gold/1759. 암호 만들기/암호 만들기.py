l,c=map(int,input().split(' '))
words=list(input().split(' '))
words.sort()
result=[]

def is_valid(password):
  vowels=list('aeiou')
  v_count=0
  for ch in password:
    if ch in vowels:
      v_count+=1
  c_count=len(password)-v_count
  return v_count>=1 and c_count>=2


def recur(start,depth):
  if depth==l:
    if is_valid(result):
      print(''.join(result))
    return 
  
  for i in range(start,c):
    result.append(words[i])
    recur(i+1,depth+1)
    result.pop()

recur(0,0)