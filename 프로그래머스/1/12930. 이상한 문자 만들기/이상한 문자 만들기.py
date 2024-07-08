def solution(s):
    words=s.split(' ')
    transformed_words = []
    for word in words:
        transformed_word = ""
        for i in range(len(word)):
            if i%2==0:
                transformed_word+=word[i].upper()
            else:
                transformed_word+=word[i].lower()
        transformed_words.append(transformed_word)
        s=' '.join(transformed_words)
        
    return s