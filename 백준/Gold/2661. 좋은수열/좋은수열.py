n=int(input())

def is_good(seq):
  length=len(seq)
  for i in range(1,length//2+1):
    if seq[-i:]==seq[-i*2:-i]:
      return False
  return True
def recur(seq):

  if len(seq)==n:
    print(seq)
    exit(0)
  
  for i in '123':
    new_seq=seq+i

    if is_good(new_seq):
      recur(new_seq)

recur('')