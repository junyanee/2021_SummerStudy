# 백준 1094
# 막대기

x = int(input())
total_length = 64
min_length = 64
count = 1

while total_length != x:
    if total_length > x:
        min_length = min_length / 2
        if total_length - min_length >= x:
            total_length = total_length - min_length
        else:
            count += 1

print(count)