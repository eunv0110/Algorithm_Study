
def solution(brown, yellow):
    cases=[]
    total=brown+yellow
    for height in range(2,int(total**0.5)+1):
        if total%height==0:
            width=total//height
            if width<height:
                continue
            #가운데 노랑색
            if (width-2)*(height-2)==yellow:
                return [width,height]