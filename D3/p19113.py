TC = int(input())
for i in range(TC):
    N = int(input())
    price_lst = list(map(int, input().split()))

    discount = []
    while price_lst:
        for j in range(len(price_lst)):
            if price_lst[j] % 4 == 0 and int(price_lst[j] * 3 / 4) in price_lst:
                original_price = price_lst.pop(j)
                discount_price = int(original_price * 3 / 4)
                price_lst.remove(discount_price)
                discount.append(discount_price)
                break

    discount.sort()
    print(f'#{i+1} {" ".join(map(str, discount))}')