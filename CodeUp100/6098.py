board = []
for i in range(12):
    board.append([])
    for j in range(12):
        board[i].append(0)

for i in range(10):
    a=input().split()
    for j in range(10):
        board[i + 1][j + 1] = int(a[j])
x = 2
y = 2
while True:
    if board[x][y] == 0:
        board[x][y] = 9
    elif board[x][y] == 2:
        board[x][y] = 9
        break
    if (board[x][y + 1] == 1 and board[x + 1][y] == 1) or (x == 9 and y == 9):
        break
    if board[x][y + 1] != 1:
        y += 1
    elif board[x + 1][y] != 1:
        x += 1

for i in range(1, 11):
    for j in range(1, 11):
        print(board[i][j], end=' ')
    print()
