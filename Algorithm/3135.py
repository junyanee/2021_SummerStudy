# 백준 3135
# 라디오

a, b = map(int, input().split())
n = int(input())
hz = []
min_val = 1001
for _ in range(n):
    hz.append(int(input()))

for h in hz:
    min_val = min(min_val, abs(h-b))

print(min(min_val + 1, abs(a - b)))