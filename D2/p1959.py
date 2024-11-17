T = int(input())

for tc in range(1, T+1):
    a, b = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    if a > b:
        A, B = B, A
        a, b = b, a

    max_sum = float('-inf')

    for i in range(b - a + 1):
        cur_sum = 0
        for j in range(a):
            cur_sum += A[j] * B[i + j]
        max_sum = max(max_sum, cur_sum)

    print(f'#{tc} {max_sum}')
