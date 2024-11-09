N = int(input())

arr = list(map(int, input().split()))

arr.sort()

idx = N // 2

print(arr[idx])