T = int(input())

for tc in range(1, T+1):
    n = int(input())

    res = 1

    for i in range(2, n+1):
        if i % 2 == 0:
            i = -1 * i
        else:
            i = i
        res = res + i

    print(f'#{tc} {res}')
    