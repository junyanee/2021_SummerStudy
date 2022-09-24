def solution(n, m, x, y, r, c, k):
    answer = ''

    # d -> l -> r -> u
    d_cnt = 0
    u_cnt = 0
    l_cnt = 0
    r_cnt = 0
    down_up = 0

    dx = r - x
    dy = c - y

    # 가능성 판별
    if k < abs(dx) + abs(dy):
        return 'impossible'
    else:
        if (k - (abs(dx) + abs(dy))) % 2 != 0:
            return 'impossible'

    # 이동거리
    down_up = n - x
    if dx > 0:
        down_up -= dx
        d_cnt += dx
    elif dx < 0:
        u_cnt -= dx

    if dy > 0:
        r_cnt += dy
    elif dy < 0:
        l_cnt -= dy

    # k를 맞추긴 위한 추가 이동거리 추가
    if k > abs(dx) + abs(dy):
        for i in range((k - (abs(dx) + abs(dy))) // 2):
            if down_up > 0:
                d_cnt += 1
                u_cnt += 1
                down_up -= 1
            else:
                r_cnt += 1
                l_cnt += 1

    # 루핑을 돌면서 검증 (그리디)
    while d_cnt > 0 or l_cnt > 0 or r_cnt > 0 or u_cnt > 0:
        if d_cnt > 0 and x + 1 <= n:
            x += 1
            d_cnt -= 1
            answer += 'd'
            continue
        if l_cnt > 0 and y - 1 > 0:
            y -= 1
            l_cnt -= 1
            answer += 'l'
            continue
        if r_cnt > 0 and y + 1 <= m:
            y += 1
            r_cnt -= 1
            answer += 'r'
            continue
        if u_cnt > 0 and x - 1 > 0:
            x -= 1
            u_cnt -= 1
            answer += 'u'
            continue

    return answer