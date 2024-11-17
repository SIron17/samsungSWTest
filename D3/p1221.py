T = int(input())

gns = {'ZRO': 0, 'ONE': 1, 'TWO': 2, 'THR': 3, 'FOR': 4, 'FIV': 5, 'SIX': 6, 'SVN': 7, 'EGT': 8, 'NIN': 9}

for _ in range(T):
    tc, n = input().split()
    n = int(n)

    s = input().split()

    sort_string = sorted(s, key=lambda x: gns[x])

    res = ' '.join(sort_string)

    print(f'{tc} {res}')
