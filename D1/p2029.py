T = int(input())

for i in range(1, T+1):
    arr = list(map(int, input().split()))
    max_val = max(arr)
    min_val = min(arr)
    arr.remove(max_val)
    arr.remove(min_val)

    avg = round(sum(arr) / len(arr))

    print(f'#{i} {avg}')