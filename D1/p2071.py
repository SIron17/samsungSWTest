T = int(input())

for i in range(1, T+1):
    arr = list(map(int, input().split()))
    res = 0
    total = sum(arr)
    res = round(total / len(arr))
    print(f'#{i} {res}')