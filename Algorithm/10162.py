# 백준 10162
# 전자레인지

# 내 풀이
A = 300
B = 60
C = 10
T = int(input())
rest = 0

sol_a = T // A
rest_1 = T % A
sol_b = rest_1 // B
rest_2 = rest_1 % B
sol_c = rest_2 // C
rest_3 = rest_2 % C
if rest_3 > 0:
    print(-1)
else:
    print(sol_a, sol_b, sol_c, end = ' ')

# 좀 더 효율적인 풀이
# T = int(input())
#
# if T % 10 != 0:
#     print(-1)
# else:
#     A = B = C = 0
#     A = T // 300
#     B = (T % 300) // 60
#     C = (T % 300) % 60 // 10
#     print(A, B, C)
