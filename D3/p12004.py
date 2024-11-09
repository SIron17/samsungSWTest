TC = int(input())

for i in range(1, TC + 1):
    N = int(input())
    found = False

    for j in range(1, 10):
        if N % j == 0:
            if 1 <= N // j <= 9:
                found = True
                break

    if found:
        print(f"#{i} Yes")
    else:
        print(f"#{i} No")