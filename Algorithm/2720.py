# 백준 2720
# 세탁소 사장 동혁

def calculate(c):
    a = list()
    q = c // 25
    rest = c % 25
    a.append(q)
    d = rest // 10
    rest = rest % 10
    a.append(d)
    n = rest // 5
    rest = rest % 5
    a.append(n)
    p = rest // 1
    a.append(p)
    print(a[0], a[1], a[2], a[3])

case = int(input())
for i in range(case):
    calculate(int(input()))


