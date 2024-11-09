T = int(input())

for i in range(1, T+1):
    S = input().strip()
    E = input().strip()

    while len(E) > len(S):
        if E[-1] == 'X':
            E = E[:-1]
        elif E[-1] == 'Y':
            E = E[:-1]
            E = E[::-1]

    print(f'#{i}', end=' ')
    if S == E:
        print("Yes")
    else:
        print("No")