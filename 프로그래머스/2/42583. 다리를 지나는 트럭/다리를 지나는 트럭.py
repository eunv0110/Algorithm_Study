from collections import deque

def solution(bridge_length, weight, truck_weights):
    bridge=deque([0]*bridge_length)
    truck=deque(truck_weights)
    current_weight=0
    answer=0
    
    while bridge:
        current_weight-=bridge.popleft()
        answer+=1
        
        if truck:
            if weight>=current_weight+truck[0]:
                new_truck=truck.popleft()
                bridge.append(new_truck)
                current_weight+=new_truck
            else:
                bridge.append(0)
    return answer