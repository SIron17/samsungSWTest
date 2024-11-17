T = int(input())

for tc in range(1, T+1):
    res = []
    cur_row = ""
    n = int(input())
    for i in range(1, n+1):
        s, num = input().split()
        num = int(num)

        repeat = s * num

        for char in repeat:
            cur_row += char

            if len(cur_row) == 10:
                res.append(cur_row)
                cur_row = ""

    if cur_row:
        res.append(cur_row)

    print(f'#{tc}')
    for line in res:
        print(line)
