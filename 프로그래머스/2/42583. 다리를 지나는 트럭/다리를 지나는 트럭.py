from collections import deque

def solution(bridge_length, weight, truck_weights):
    #bridge_length : 최대 올라갈수 있는 트럭 개수
    #weight : 견딜 수 있는 최대 무게
    #truck_wights : 트럭별 무게
    
    bridge=deque([0]*bridge_length)
    truck=deque(truck_weights)
    current_weight=0
    time=0
    
    while bridge:
        
        current_weight-=bridge.popleft()
        time+=1
        
        if truck:
            if weight>=truck[0]+current_weight:
                new_truck=truck.popleft()
                bridge.append(new_truck)
                current_weight+=new_truck
            else:
                bridge.append(0)     
    
    return time