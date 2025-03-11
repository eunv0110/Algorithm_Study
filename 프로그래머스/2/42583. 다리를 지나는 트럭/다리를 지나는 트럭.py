from collections import deque
def solution(bridge_length, weight, truck_weights):
    #bridge_length:다리에 올라갈 수 있는 트럭수
    #weight: 다리가 견딜 수 있는 무게
    #truck_weights:트럭별 무게
    
    bridge=deque([0]*bridge_length)
    truck=deque(truck_weights)
    current_weight=0
    time=0
    
    while bridge:
        current_weight-=bridge.popleft()
        time+=1
        
        #대기 트럭이 남아있는 경우
        if truck:
            if current_weight+truck[0]<=weight:
                new_truck=truck.popleft()
                bridge.append(new_truck)
                current_weight+=new_truck
            else:
                bridge.append(0)
            
    return time