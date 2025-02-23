def solution(s, n):
    alphabet='abcdefghijklmnopqrstuvwxyz'
    ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    answer=[]
    
    for i in s:
        if i in alphabet:
            idx=(alphabet.index(i)+n)%26
            answer.append(alphabet[idx])
        elif i in ALPHABET:
            idx=(ALPHABET.index(i)+n)%26
            answer.append(ALPHABET[idx])
        else:
            answer.append(i)
            
            
    return ''.join(answer)