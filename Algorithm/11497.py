# 백준 11497
# 통나무 건너뛰기

T = int(input())

for _ in range(T):
    N = int(input())
    L = list(map(int, input().split()))
    L.sort()
    res = 0
    for i in range(2, N):
        res = max(res, abs(L[i] - L[i-2]))
    print(res)

