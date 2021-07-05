sum = 0
count = 1
a = int(input())
while sum < a:
    sum += count
    count += 1
    if sum >= a:
        break;
print(sum)