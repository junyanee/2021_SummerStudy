# 백준 12927
# 배수 스위치

bulbs = list(input())
bulbs.insert(0, 'N')

count = 0

for i in range(1, len(bulbs)):
    if bulbs[i] == 'Y':
        for j in range(i, len(bulbs), i):
            if bulbs[j] == 'Y':
                bulbs[j] = 'N'
            else:
                bulbs[j] = 'Y'
        count += 1

print(count)