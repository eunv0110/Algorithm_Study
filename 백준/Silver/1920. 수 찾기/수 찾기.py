from bisect import bisect_left

n = int(input())
arr = sorted(list(map(int, input().split())))  # ✅ 정렬 필수
m = int(input())
nums = list(map(int, input().split()))

for num in nums:
    idx = bisect_left(arr, num)
    if idx < n and arr[idx] == num:
        print(1)
    else:
        print(0)
