for i in range(1, 11):
    T = int(input())
    arr = list(map(int, input().split()))

    while True:
        for j in range(1, 6):
            if arr[0] - j > 0:
                arr.append(arr[0] - j)
                arr.remove(arr[0])
            else:
                arr.append(0)
                arr.remove(arr[0])
                print(f"#{T}", *arr)
                break
        if arr[-1] == 0:
            break