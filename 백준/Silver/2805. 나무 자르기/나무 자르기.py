def get_wood_amount(trees, cut_height):
    """주어진 절단기 높이로 얻을 수 있는 나무의 총 길이를 계산"""
    return sum(tree - cut_height for tree in trees if tree > cut_height)

def find_max_cut_height(trees, required_wood):
    """이진 탐색을 사용해 필요한 나무를 얻기 위한 최대 절단기 높이를 찾는다"""
    low, high = 0, max(trees)
    result = 0
    
    while low <= high:
        mid = (low + high) // 2
        wood = get_wood_amount(trees, mid)
        
        if wood >= required_wood:
            result = mid  # 더 높은 절단기 높이를 탐색
            low = mid + 1
        else:
            high = mid - 1
    
    return result

# 입력 처리
import sys
input = sys.stdin.read
data = input().split()

N = int(data[0])
M = int(data[1])
trees = list(map(int, data[2:]))

# 결과 계산 및 출력
print(find_max_cut_height(trees, M))

