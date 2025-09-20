import sys

N=int(input())

def is_good(seq):
  length=len(seq)
  for k in range(1,length//2+1):
    if seq[-k:]==seq[-2*k:-k]:
      return False
  return True

def recur(seq):
  if N==len(seq):
    print(seq)
    sys.exit(0)
  for num in '123':
    if is_good(seq+num):
      recur(seq+num)

recur('')