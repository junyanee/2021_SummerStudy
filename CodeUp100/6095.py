checkBoard = []
for i in range(20):
    checkBoard.append([])
    for j in range(20):
        checkBoard[i].append(0)

n = int(input())
for i in range(n):
    white_x, white_y = map(int, input().split())
    checkBoard[white_x][white_y] = 1

for i in range(1, 20):
    for j in range(1, 20):
        print(checkBoard[i][j], end = ' ')
    print()