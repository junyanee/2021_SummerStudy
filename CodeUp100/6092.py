n = int(input())
a = list(map(int, input().split()))
b = []
for i in range(24):
    b.append(0)
for i in range(n):
    b[a[i]] += 1
for i in range(1, 24):
    print(b[i], end = ' ')