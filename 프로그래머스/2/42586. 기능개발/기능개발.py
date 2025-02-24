def solution(progresses, speeds):
    answer = []
    #progresses가 빌때까지 반복
    while progresses:
        #배포 가능한 개수
        count=0
        
        #작업 리스트가 남아있고 맨 앞의 작업의 진도가 100인경우 : 기능 배포 변수 증가
        while progresses and progresses[0]>=100:
            count+=1
            progresses.pop(0)
            speeds.pop(0)
        #작업 리시트의 진도 증가
        progresses=[progresses[i]+speeds[i] for i in range(len(progresses))]
        
        if count:
            answer.append(count)
    return answer