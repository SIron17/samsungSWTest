T = 10

for tc in range(1, T + 1):
    n = int(input())
    s = input().strip()
    string = input().strip()
    cnt = string.count(s)

    print(f'#{tc} {cnt}')
