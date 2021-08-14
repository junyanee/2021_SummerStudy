# 백준 11256
# 사탕

T = int(input())
for t in range(T):
    J, N = map(int, input().split())

    boxes = []
    for box_num in range(N):
        Ri, Ci = map(int, input().split())
        box = Ri * Ci
        boxes.append(box)

    boxes.sort(reverse=True)

    candy = 0
    for box_index in range(len(boxes)):
        candy += boxes[box_index]

        if candy >= J:
            print(box_index + 1)
            break