def solution(my_string):
    gather=['a','e','i','o','u']
    for vowel in gather:
        my_string=my_string.replace(vowel,'')

    return my_string