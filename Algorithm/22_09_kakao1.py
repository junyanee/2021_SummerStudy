from datetime import datetime
from dateutil.relativedelta import relativedelta

def solution(today, terms, privacies):

    answer = []
    termsToList = []
    privacy = []
    todayToDate = datetime.strptime(today, '%Y.%m.%d')

    # 띄어쓰기 잘라서 리스트에 따로 저장
    for term in terms:
        termsToList.append(term.split())

    # 띄어쓰기 잘라서 리스트에 따로 저장
    for x in privacies:
        privacy.append(x.split())

    # privacies 돌면서 날짜 Date로 변환하고 계산
    for idx, val in enumerate(privacy):
        agreeDay = datetime.strptime(val[0], '%Y.%m.%d')
        for term in termsToList:
            if val[1] in term:
                val[1] = termsToList.index(term)
                month = int(termsToList[val[1]][1])
                if todayToDate >= agreeDay + relativedelta(months = month):
                    answer.append(idx + 1)

    return answer