N = int(input())

for i in range(1, N + 1):
    cnt = str(i).count('3') + str(i).count('6') + str(i).count('9')

    if cnt > 0:
        print('-' * cnt, end=' ')
    else:
        print(i, end=' ')