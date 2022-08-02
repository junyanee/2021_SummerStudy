def solution(periods, payments, estimates):

    vip = [0] * len(periods)
    xvip = [0] * len(periods)
    payCheck = 0

    for i in range(len(periods)):

        payCheck = sum(payments[i], estimates[i]) - payments[i][0]
        if periods[i] == 23:
            # xvip -> vip
            if payCheck >= 900000:
                vip[i] += 1
        elif periods[i] == 59:
            # xvip -> vip
            if sum(payments[i]) <= 600000 & payCheck >= 600000:
                vip[i] += 1
            # vip -> xvip
            if sum(payments[i]) <= 600000 & payCheck < 600000:
                xvip[i] += 1
        elif 24 <= periods[i] <= 60:
            # xvip -> vip
            if sum(payments[i]) <= 900000 & payCheck >= 900000:
                vip[i] += 1
            # vip -> xvip
            elif sum(payments[i]) >= 900000 & payCheck < 900000:
                xvip[i] += 1
        elif periods[i] >= 60:
            # xvip -> vip
            if sum(payments[i]) <= 600000 & payCheck >= 600000:
                vip[i] += 1
            # vip -> xvip
            elif sum(payments[i]) >= 600000 & payCheck < 600000:
                xvip[i] += 1

    payCheck = 0

    answer = [sum(vip), sum(xvip)]
    return answer

print(solution([20, 23, 24], [[100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000], [100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000], [350000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000]], [100000, 100000, 100000]))
print(solution([24, 59, 59, 60], [[50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000], [50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000], [350000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000], [50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000]], [350000, 50000, 40000, 50000]))