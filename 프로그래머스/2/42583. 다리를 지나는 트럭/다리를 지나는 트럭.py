from collections import deque

def solution(bridge_length, weight, truck_weights):
    bridge=deque([0]*bridge_length)
    trucks=deque(truck_weights) #대기트럭
    current_weight=0
    time=0
    
    #다리에 트럭이 없을때까지
    while bridge:
        time+=1
        current_weight-=bridge.popleft()
        
        #만약에 대기 트럭이 있는 경우
        if trucks:
            if current_weight+trucks[0]<=weight:
                new_truck=trucks.popleft()
                bridge.append(new_truck)
                current_weight+=new_truck
            else:
                bridge.append(0)
                
    return time