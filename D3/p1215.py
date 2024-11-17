def is_palindrome(s):
    return s == s[::-1]

def count_palindromes(board, length):
    cnt = 0

    for row in board:
        for i in range(9 - length):
            if is_palindrome(row[i:i+length]):
                cnt += 1

    for col in range(8):
        for i in range(9 - length):
            string = ''.join(board[row][col] for row in range(i, i+length))
            if is_palindrome(string):
                cnt += 1
    return cnt

for tc in range(1, 11):
    length = int(input())
    board = [input().strip() for _ in range(8)]
    res = count_palindromes(board, length)
    print(f'#{tc} {res}')
