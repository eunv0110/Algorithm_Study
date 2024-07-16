def solution(answers):
    first=[1,2,3,4,5]
    second=[2,1,2,3,2,4,2,5]
    thrid=[3,3,1,1,2,2,4,4,5,5]
    first_answer,second_answer,thrid_answer=0,0,0
    
    
    for idx,answer in enumerate(answers):
        if answer==first[idx%len(first)]:
            first_answer+=1
        if answer==second[idx%len(second)]:
            second_answer+=1
        if answer==thrid[idx%len(thrid)]:
            thrid_answer+=1
    
    max_score=max(first_answer,second_answer,thrid_answer)
    result=[]
    if max_score==first_answer:
        result.append(1)
    if max_score==second_answer:
        result.append(2)
    if max_score==thrid_answer:
        result.append(3)
    return result

        
        
        