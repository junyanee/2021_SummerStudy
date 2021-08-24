# 프로그래머스
# 두 개 뽑아서 더하기

numbers = list(map(int, input()))
result = []

for i in range(len(numbers)):
    for j in range(i, len(numbers)):
        if i != j:
            added = numbers[i] + numbers[j]
            if added not in result:
                result.append(added)

result.sort()
print(result)