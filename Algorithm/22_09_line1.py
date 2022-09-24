from typing import List

def solution(queries: List[List[int]]) -> int:

# 배열 번호 저장
    #배열 번호 체크할 numList
    wholeList = [[0,0,0] for i in range (1000)]
    count = 0
    numList = []
    for x in queries:
        if x[0] not in numList:
            numList.append(x[0])
            wholeList[x[0]-1][0] = x[0]
            wholeList[x[0]-1][1] = x[1]
            wholeList[x[0]-1][2] = findNum(x[1])
        else:
            if wholeList[x[0]-1][1] + x[1] > wholeList[x[0]-1][2]:
                wholeList[x[0]-1][2] = (wholeList[x[0]-1][2])*2
                count += wholeList[x[0]-1][1]
                wholeList[x[0]-1][1] = wholeList[x[0]-1][1] + x[1]
            else:
                wholeList[x[0]-1][1] = wholeList[x[0]-1][1] + x[1]
    return count

def findNum(n):
    k = 1
    while k < n:
        k = k << 1
    return k