def solution(a, b):
    a,b=str(a),str(b)
    answer=int(a+b)
    answer2 = int(b+a)
    if answer>answer2:
        return answer
    else:
        return answer2
