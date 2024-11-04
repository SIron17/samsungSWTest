T = int(input())

for i in range(1, T+1):
    arr = list(map(int, input().split()))
    res = 0
    for j in range(len(arr)):
        if int(arr[j] % 2) != 0:
            res += arr[j]

    print(f'#{i} {res}')