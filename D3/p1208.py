for tc in range(1, 11):
    dump = int(input())
    arr = list(map(int, input().split()))

    while dump > 0:
        max_index = arr.index(max(arr))
        min_index = arr.index(min(arr))

        if arr[max_index] - arr[min_index] <= 1:
            break

        arr[max_index] -= 1
        arr[min_index] += 1
        dump -= 1

    res = max(arr) - min(arr)

    print(f'#{tc} {res}')
