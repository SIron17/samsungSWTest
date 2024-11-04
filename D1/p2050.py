n = input()
res = []

for char in n:
    num = ord(char.lower()) - ord('a') + 1
    res.append(str(num))

print(" ".join(res))