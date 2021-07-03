# 백준 9237
# 이장님 초대

tree = int(input())
days = list(map(int, input().split()))
days.sort(reverse = True)
max_day = 0

for i in range(len(days)):
    growing_day = days[i] + (i+1)
    if max_day < growing_day:
        max_day = growing_day

print(max_day + 1)