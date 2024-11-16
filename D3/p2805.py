T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    # NxN 크기의 농장 정보 입력 받기
    # 각 줄마다 문자열로 입력받아 각 자리수를 정수로 변환하여 2차원 리스트로 저장
    arr = [list(map(int, list(input()))) for _ in range(N)]

    cost = 0

    # 마름모 중앙값 계산
    mid = N // 2

    # 마름모의 위쪽 삼각형 부분 계산
    # i는 행 번호, 위에서부터 중앙까지
    for i in range(mid + 1):
        # j는 각 행에서 수확할 열의 범위
        # 중앙에서 i만큼 좌우로 퍼져나감
        for j in range(mid - i, mid + i + 1):
            cost += arr[i][j]

    # 마름모의 아래쪽 삼각형 부분 계산
    # i는 행 번호, 중앙 다음부터 맨 아래까지
    for i in range(mid + 1, N):
        # j는 각 행에서 수확할 열의 범위
        # 아래로 갈수록 범위가 좁아짐
        for j in range(i - mid, N - (i - mid)):
            cost += arr[i][j]

    print(f'#{tc} {cost}')