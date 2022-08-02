#1. 선택정렬

def solution(p):
    result = [0] * len(p)

    i = 0
    for i in range(len(p)):
        min_idx = i
        flag = 0

        for j in range(i + 1, len(p)):
            if p[min_idx] > p[j]:
                min_idx = j
                flag = 1

        p[i], p[min_idx] = p[min_idx], p[i]

        if flag == 1:
            result[i] += 1
            result[min_idx] += 1

    return result

print(solution([2,5,3,1,4]))
print(solution([2,3,4,5,6,1]))
print(solution([1,2,3,4,5,6,7,8,9]))