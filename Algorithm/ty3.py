# 문제4
# 로또 번호 맞추기 프로그램을 작성해보자
# 1. 로또 번호는 중복없이 랜던하게 4개 생성한다 random.sample()
# 2. 사용자에게 4개의 수를 입력받는다 split()
# 3. 4개의 수를 모두 맞추면 당첨을 출력하고 그렇지 않으면 꽝 출력
# 4. 맞춘개수, 로또번호, 맞춘 번호를 출력한다
# 실행결과 4개수를 입력 40 25 32 18
# 꽝! 맞춘개수 0 로또번호 [42, 26, 14, 17] 맞춘번호 0

import random

lotto = random.sample(range(1, 45), 4)
count = []
print(lotto)

numList = list(map(int, input('4개의 수를 입력하세요.').split()))

count = set(lotto) & set(numList)
if len(count) == 4:
    print('당첨')
else:
    print('꽝')
print('맞춘개수', len(count))
print('로또번호', lotto)
if len(count) == 0:
    print('맞춘번호', 0)
else:
    print('맞춘번호', count)



