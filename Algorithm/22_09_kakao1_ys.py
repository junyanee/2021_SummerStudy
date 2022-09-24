def solution(today, terms, privacies):
    answer = []

    arr = []

    tmp_today = today.split(".")
    year_today = int(tmp_today[0])
    month_today = int(tmp_today[1])
    day_today = int(tmp_today[2])

    # term 등록
    terms_dic = {}
    for row in terms:
        tmp = row.split()
        terms_dic[tmp[0]] = int(tmp[1])

    for i, privacy in enumerate(privacies):
        tmp = privacy.split()
        term = terms_dic[tmp[1]]

        tmp_day = tmp[0].split(".")
        year = int(tmp_day[0])
        month = int(tmp_day[1])
        day = int(tmp_day[2])

        # 유효기간을 더한후 달, 연 계산
        month += term
        if month > 12:
            year += month // 12
            month %= 12
            if month == 0:
                year -= 1
                month = 12

        # 유효기간이 지났는지 판별
        if year_today > year :
            answer.append(i+1)
        elif year_today == year :
            if month_today > month :
                answer.append(i+1)
            elif month_today == month :
                if day_today >= day :
                    answer.append(i+1)

    return answer