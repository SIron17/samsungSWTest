T = 10

for tc in range(1, T + 1):
    N = int(input())
    b = list(map(int, input().split()))

    cnt = 0

    # 맨 왼쪽 2칸, 맨 오른쪽 2칸을 제외한 모든 건물 확인
    for i in range(2, N - 2):
        cur = b[i] # 현재 건물 높이

        # 현재 건물 높이 0이면 다음 건물로
        if cur == 0:
            continue

        # 좌우 2칸 내의 가장 높은 건물 높이 확인
        max_val = max(
            b[i-2], b[i-1],
            b[i+1], b[i+2]
        )

        if cur > max_val:
            cnt += cur - max_val

    print(f'#{tc} {cnt}')