# 백준 1002
# 터렛

case = int(input())
for i in range(case):
    b = list(map(int, input().split()))
    distance = ((b[0] - b[3])**2 + (b[1] - b[4])**2)**(1/2)
    if distance == 0:
        if b[2] == b[5]:
            print(-1)
        else:
            print(0)
    elif distance < abs(b[2] - b[5]):
        print(0)
    elif distance == abs(b[2] - b[5]):
        print(1)
    elif b[2] + b[5] < distance:
        print(0)
    elif b[2] + b[5] == distance:
        print(1)
    else:
        print(2)