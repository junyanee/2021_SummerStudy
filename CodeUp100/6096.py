# 아무리 봐도 헷갈린다...
# 다시 몇번 들여다 봐야할것같다

checkBoard = []
for i in range(19):
    checkBoard.append([])
    for j in range(19):
        checkBoard[i].append(0)

for i in range(19):
    checkBoard[i] = list(map(int, input().split()))

n = int(input())
for i in range(n):
    x, y = map(int, input().split())
    for j in range(19):
        if checkBoard[x-1][j] == 0:
            checkBoard[x-1][j] = 1
        else:
            checkBoard[x-1][j] = 0
        if checkBoard[j][y-1] == 0:
            checkBoard[j][y-1] = 1
        else:
            checkBoard[j][y-1] = 0

for i in range(19):
    for j in range(19):
        print(checkBoard[i][j], end = ' ')
    print()