# 프로그래머스
# 서울에서 김서방 찾기

def solution(seoul):
    answer = ''
    idx = 0
    if "Kim" in seoul:
        idx = seoul.index("Kim")
        answer = "김서방은 " + str(idx) + "에 있다"

    return answer
