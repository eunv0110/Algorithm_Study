from collections import deque
#bridge_length는 최대 트럭
#weight 최대 무게
#truck_weights 트럭 무게
def solution(bridge_length, weight, truck_weights):
  bridge=deque([0]*bridge_length)
  time=0
  truck_weights=deque(truck_weights)
  current_weight=0

  #대기중인 트럭이 있고 현재무게가 0보다 클때까지
  while current_weight>0 or truck_weights:
    time+=1

    #트럭이 현재 다리에서 빠져나옴
    truck=bridge.popleft() #빠져나온 트럭 무게
    current_weight-=truck #현재무게에서 빠져나온 트럭 무게 빼기

    #조건에 맞는 트럭무게가 최대 무게보다 작고 아직 모든 트럭이 빠지지 않았으면
    if truck_weights and weight>=(truck_weights[0]+current_weight):
      new_truck=truck_weights.popleft()
      bridge.append(new_truck) #대기중인 트럭을 하나 뺌
      current_weight+=new_truck #새 트럭 추가
    
    else:
      bridge.append(0)

  return time