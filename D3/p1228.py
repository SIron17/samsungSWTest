T = 10
for tc in range(1, T + 1):
    N = int(input())
    password = list(map(int, input().split()))
    M = int(input())
    cmd = list(input().split())

    i = 0
    while i < len(cmd):
        if cmd[i] == 'I':
            x = int(cmd[i + 1])
            y = int(cmd[i + 2])

            s = list(map(int, cmd[i + 3:i + 3 + y]))
            password[x:x] = s

            i += (3 + y)

    print(f'#{tc}', *password[:10])
