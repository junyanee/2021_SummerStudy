# 진법 변환

# n 진수 -> 10진수
# int(string, base)
# string에는 n진수 값을, base 에는 진법을 넣으면 됨
print(int('100',2))
print(int('221',3))
print(int('712',8))
print(int('A15E',16))
print(int('423',5))

# 10진수 -> 2, 8, 16진수
# 진법 표시를 지우려면 [2:] 으로
print(bin(25))
print(oct(25))
print(hex(25))
print(bin(25)[2:])
print(oct(25)[2:])
print(hex(25)[2:])

# 10진수 -> n 진수
def solution(n, q):
    rev_base = ''

    while n > 0:
        n, mod = divmod(n,q)
        rev_base += str(mod)

    return rev_base[::-1]
    # 역순인 진수를 뒤집어 반환
print(solution(45,3))