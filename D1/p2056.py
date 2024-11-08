T = int(input())

days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for i in range(1, T + 1):
    s = input()
    y, m, d = int(s[:4]), int(s[4:6]), int(s[6:8])

    print(f'#{i}', end=' ')

    if m < 1 or m > 12:
        print('-1')

    elif d < 1 or d > days_in_month[m]:
        print('-1')
    else:
        print(f'{y:04}/{m:02}/{d:02}')