# 백준 14655
# 욱제는 도박쟁이야!!

n = int(input())
round_1 = list(map(int, input().split()))
round_2 = list(map(int, input().split()))
ans = 0

for i in round_1:
    if i < 0:
        i = -i
        ans += i
    else:
        ans += i

for i in round_2:
    if i > 0:
        i = -i
        ans -= i
    else:
        ans -= i
print(ans)
