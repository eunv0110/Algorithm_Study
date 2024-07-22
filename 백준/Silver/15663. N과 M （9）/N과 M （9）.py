from itertools import permutations

def main():
    # 입력을 받습니다.
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))

    # permutations 함수를 이용하여 길이가 M인 모든 순열을 구합니다.
    all_permutations = permutations(numbers, M)

    # 집합을 사용하여 중복을 제거하고, 리스트로 변환하여 정렬합니다.
    unique_permutations = sorted(set(all_permutations))

    # 각 순열을 출력합니다.
    for perm in unique_permutations:
        print(" ".join(map(str, perm)))

if __name__ == "__main__":
    main()
