# 백준 1434
# 책 정리

n, m = map(int, input().split())
box = list(map(int, input().split()))
book = list(map(int, input().split()))

result = 0
num_x = 0
num_k = 0

while(1):
    if num_x >= n or num_k >= m:
        break
    if box[num_x] >= book[num_k]:
        box[num_x] = box[num_x] - book[num_k]
        num_k += 1
        continue

    else:
        num_x += 1

print(sum(box))