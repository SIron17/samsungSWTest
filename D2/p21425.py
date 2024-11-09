T = int(input())

for _ in range(T):
    a, b, n = map(int, input().split())

    cnt = 0

    while a <= n and b <= n:
        if a < b:
            a += b
            cnt += 1
            if a > n:
                print(cnt)
        else:
            b += a
            cnt += 1
            if b > n:
                print(cnt)