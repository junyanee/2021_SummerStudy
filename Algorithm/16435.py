# 백준 16435
# 스네이크버드

N, L = map(int, input().split())
h = list(map(int, input().split()))
h.sort()

for i in h:
    if i <= L:
        L += 1
print(L)