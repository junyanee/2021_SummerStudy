# 1부터 100까지의 곱을 구하는 중에 곱이 5000을 넘을 때의 곱의 값과 5000을 넘게 한 숫자를 출력하는 프로그램을 작성하시오.
# <실행결과>
# 곱이ㅣ 5000을 넘을 때 곱의 값 : 5040
# 곱이 5000을 넘게 만든 수 : 7

result = 1
num = 1
while result < 5000:
    result = result * num
    if result > 5000:
        print(result, num)
        break
    else:
        num += 1
