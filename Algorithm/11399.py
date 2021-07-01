# 백준 11399
# ATM

case = int(input())
a = list(map(int, input().split()))
a.sort()

time = 0
for i in range(case):
    for j in range(i+1):
        time += a[j]

print(time)