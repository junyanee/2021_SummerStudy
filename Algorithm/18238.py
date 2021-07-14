# 백준 18238
# ZOAC 2

string = input()
start = 'A'
res = 0

for i in string:
    left = ord(i) - ord(start)
    right = ord(start) - ord(i)

    if left < 0:
        left += 26
    elif right < 0:
        right += 26

    res += min(left, right)
    start = i

print(res)