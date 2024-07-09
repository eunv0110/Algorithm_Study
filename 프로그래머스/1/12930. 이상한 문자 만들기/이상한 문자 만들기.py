def solution(s):
    s_list=s.split(' ')
    transformed_words=[]
    for word in s_list:
        transformed_word=[]
        for i in range(len(word)):
            if i%2==0:
                transformed_word.append(word[i].upper())
                
            else:
                transformed_word.append(word[i].lower())
        transformed_words.append(''.join(transformed_word))
        answer=' '.join(transformed_words)
    return answer
            
            