# 백준 20044
# Project Teams

n = int(input())
w = list(map(int, input().split()))
w.sort()
res = []
for i in range(n):
    a = w[i] + w[2 * n - i - 1]
    res.append(a)

print(min(res))