T = int(input())

for i in range(1, T + 1):
    A, B = input().split()

    if A == B:
        result = A
    else:
        result = '1'

    print(f"#{i} {result}")