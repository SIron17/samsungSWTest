T = 10

for tc in range(1, T + 1):
    n = int(input())
    arr = []
    max_sum = 0

    # 배열 입력
    for _ in range(100):
        row = list(map(int, input().split()))
        arr.append(row)

    # 행 합 계산
    for i in range(100):
        row_sum = sum(arr[i])
        max_sum = max(max_sum, row_sum)

    # 열 합 계산
    for j in range(100):
        col_sum = 0
        for i in range(100):
            col_sum += arr[i][j]
        max_sum = max(max_sum, col_sum)

    # 왼쪽에서 오른쪽 대각선 계산
    왼오대각선 = 0
    for i in range(100):
        왼오대각선 += arr[i][i]
    max_sum = max(max_sum, 왼오대각선)

    # 오른쪽에서 왼쪽 대각선 계산
    오왼대각선 = 0
    for i in range(100):
        오왼대각선 += arr[i][99-i]
    max_sum = max(max_sum, 왼오대각선)

    print(f'#{tc} {max_sum}')

