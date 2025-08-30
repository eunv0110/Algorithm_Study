from collections import deque

def solution(bridge_length, weight, truck_weights):
    time=0
    current_weight=0
    bridge=deque(bridge_length*[0])
    truck=deque(truck_weights)
    
    while bridge:
        time+=1
        #맨 앞 칸 하나 제거
        current_weight-=bridge.popleft()
        
        if truck:
            if weight>=truck[0]+current_weight:
                new_truck=truck.popleft()
                bridge.append(new_truck)
                current_weight+=new_truck
            else:
                bridge.append(0)

                
    return time