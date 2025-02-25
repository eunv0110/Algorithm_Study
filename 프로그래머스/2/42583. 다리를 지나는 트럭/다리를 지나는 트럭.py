from collections import deque
def solution(bridge_length, weight, truck_weights):
    time = 0
    truck_weights=deque(truck_weights)
    bridge=deque([0]*bridge_length)
    current_weight=0
    
    #대기중인 트럭 있고 현재무게가 0보다 클때까지
    while truck_weights or current_weight>0:
        time+=1
        
        #다리에서 트럭이 빠져나옴
        exited_truck=bridge.popleft() #빠져나온 트럭 무게
        #현재 무게에서 빠져나온 무게 빼줌
        current_weight-=exited_truck
        
        #새로운 트럭을 올릴 수 있는지 체크
        #truck 비어있지 않고 크고 최대 무게보다 작을때
        if truck_weights and (current_weight+truck_weights[0]<=weight):
            new_truck=truck_weights.popleft() #대기 중인 트럭 하나 뺌
            bridge.append(new_truck) #다리 위에 새로운 트럭 추가
            current_weight+=new_truck
        else:
            bridge.append(0) #트럭 위에 못 올라가면 0 추가
            
    return time