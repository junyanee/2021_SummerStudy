# 백준 13904
# 과제

n = int(input())
homeworks = []
for i in range(n):
    d, w = map(int, input().split())
    homeworks.append((d,w))
homeworks.sort()

todo = []
date = homeworks[-1][0]
ans = 0

while True:
    if date == 0:
        break
    while homeworks and homeworks[-1][0] >= date:
        todo.append(homeworks.pop()[1])
    date -= 1
    if not todo:
        continue
    todo.sort()
    ans += todo.pop()
print(ans)
