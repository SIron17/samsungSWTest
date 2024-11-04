T = int(input())

for i in range(1, T+1):
    N = int(input())
    prices = list(map(int, input().split()))

    max_profit = 0
    max_price = 0

    for price in reversed(prices):
        if price > max_price:
            max_price = price
        else:
            max_profit += max_price - price

    print(f'#{i} {max_profit}')