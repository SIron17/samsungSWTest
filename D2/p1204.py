from collections import Counter

T = int(input())

for _ in range(T):
    cnt = 0
    n = int(input())
    arr = list(map(int, input().split()))

    counter = Counter(arr)
    max_val = max(counter.values())

    modes = [key for key, value in counter.items() if value == max_val]

    if len(modes) >= 1:
        res = max(modes)

    print(f'#{n} {res}')