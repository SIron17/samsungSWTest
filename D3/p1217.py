def func(x, y):
    if y == 1:
        return x
    return x * func(x, y-1)

T = 10

for tc in range(1, T + 1):
    N = int(input())
    a, b = map(int, input().split())
    res = func(a, b)
    print(f'#{tc} {res}')
