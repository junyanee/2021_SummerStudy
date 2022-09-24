def solution(cap, n, deliveries, pickups):
    answer = 0

    for i in range(n - 1, -1, -1):
        if deliveries[i] > 0:
            break
    for j in range(n - 1, -1, -1):
        if pickups[j] > 0:
            break

    if i == 0 and j == 0:
        return 0

    while i >= 0 or j >= 0:
        answer += (max(i, j) + 1) * 2
        i = get_i_and_adjust_list(deliveries, cap, i)
        j = get_i_and_adjust_list(pickups, cap, j)

    return answer


def get_i_and_adjust_list(house_list, cap, i):
    cur_cap = 0
    while cur_cap < cap and i >= 0:
        if house_list[i] + cur_cap > cap:
            gap = cap - cur_cap
            cur_cap = cap
            house_list[i] -= gap
        else:
            cur_cap += house_list[i]
            house_list[i] = 0
            i -= 1
    while house_list[i] == 0 and i >= 0:
        i -= 1
    return i