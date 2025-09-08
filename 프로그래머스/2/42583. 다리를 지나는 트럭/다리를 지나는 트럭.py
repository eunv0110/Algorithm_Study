from collections import deque
def solution(bridge_length, weight, truck_weights):
    bridge=deque(bridge_length*[0])
    truck=deque(truck_weights)
    current_weight=0 #현재 무게
    time=0
    while bridge:
        current_weight-=bridge.popleft() #bridge에서 하나 없애기
        time+=1
        if truck:
            if weight>=current_weight+truck[0]:
                new_truck=truck.popleft()
                current_weight=new_truck+current_weight
                bridge.append(new_truck)
            else:
                bridge.append(0)
    return time