# 백준 1003
# 피보나치 함수

cntZero = [1, 0]
cntOne = [0, 1]

for i in range(2, 41):
    cntZero.append(cntZero[i-1] + cntZero[i-2])
    cntOne.append(cntOne[i-1] + cntOne[i-2])

case = int(input())
for i in range(case):
    n = int(input())
    print(cntZero[n], cntOne[n])