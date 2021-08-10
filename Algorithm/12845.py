# 백준 12845
# 모두의 마블

n = int(input())
L = list(map(int, input().split()))

maxIdx = -1
Max = 0
Sum = 0

for i in range(len(L)):
    if L[i] > Max:
        maxIdx = i
        Max = L[i]

L.pop(maxIdx)

for elem in L:
    Sum += elem

Sum += Max * (n-1)
print(Sum)
