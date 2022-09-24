from itertools import product

def solution(users, emoticons):
    answer = []

    count_max = 0
    fee_max = 0

    for rates in product([10,20,30,40], repeat=len(emoticons)):
        cnt = 0
        total = 0
        for user in users:
            fee = 0
            for i, rate in enumerate(rates):
                if rate >= user[0]:
                    fee += int((100 - rate) * 0.01 * emoticons[i])
            if fee >= user[1]:
                cnt += 1
            else:
                total += fee
        if count_max < cnt:
            count_max = cnt
            fee_max = total
        elif count_max == cnt and fee_max < total:
            fee_max = total

    answer.append(count_max)
    answer.append(fee_max)

    return answer