from collections import defaultdict

DATA = "DATA"
KEY = "KEY"

chart = defaultdict(lambda: None)
answer = []
key = 0


def solution(commands):
    for command in commands:
        c = command.split()
        if c[0] == 'UPDATE':
            if len(c) == 4:
                update(int(c[1]), int(c[2]), c[3])
            elif len(c) == 3:
                update_all(c[1], c[2])
        elif c[0] == 'MERGE':
            merge(int(c[1]), int(c[2]), int(c[3]), int(c[4]))
        elif c[0] == 'UNMERGE':
            unmerge(int(c[1]), int(c[2]))
        elif c[0] == 'PRINT':
            _print(int(c[1]), int(c[2]))
    return answer


def select(r, c):
    cand = (r, c)
    while True:
        nxt_cand = chart[cand]
        if not is_key(nxt_cand):
            return nxt_cand
        cand = nxt_cand


def get_final_key(r, c):
    cand = (r, c)
    while True:
        nxt_cand = chart[cand]
        if not is_key(nxt_cand):
            return cand
        cand = nxt_cand


def update(r, c, new_value):
    final_key = get_final_key(r, c)
    chart[final_key] = new_value


def update_all(value1, value2):
    for key in chart.keys():
        if type(key) == tuple:
            if select(key[0], key[1]) == value1:
                final_key = get_final_key(key[0], key[1])
                chart[final_key] = value2


def merge(r1, c1, r2, c2):
    global key

    val1 = select(r1, c1)
    val2 = select(r2, c2)
    if val1 is not None and val2 is not None:
        merge_val = val1
    elif val1 is not None and val2 is None:
        merge_val = val1
    elif val1 is None and val2 is not None:
        merge_val = val2
    else:
        merge_val = None

    key += 1
    chart[key] = merge_val

    final_key1 = get_final_key(r1, c1)
    final_key2 = get_final_key(r2, c2)
    chart[final_key1] = key
    chart[final_key2] = key


def unmerge(r, c):
    prev_val = select(r, c)
    final_key = get_final_key(r, c)
    chart[final_key] = None
    chart[(r, c)] = prev_val


def _print(r, c):
    global answer
    val = select(r, c)
    if val is None:
        answer.append('EMPTY')
    else:
        answer.append(val)


def is_key(val):
    return type(val) == int


if __name__ == "__main__":
    # print(solution(
    #     [
    #         "UPDATE 1 1 menu",
    #         "UPDATE 1 2 category",
    #         "UPDATE 2 1 bibimbap",
    #         "UPDATE 2 2 korean",
    #         "UPDATE 2 3 rice",
    #         "UPDATE 3 1 ramyeon",
    #         "UPDATE 3 2 korean",
    #         "UPDATE 3 3 noodle",
    #         "UPDATE 3 4 instant",
    #         "UPDATE 4 1 pasta",
    #         "UPDATE 4 2 italian",
    #         "UPDATE 4 3 noodle",
    #         "MERGE 1 2 1 3",
    #         "MERGE 1 3 1 4",
    #         "UPDATE korean hansik",
    #         "UPDATE 1 3 group",
    #         "UNMERGE 1 4",
    #         "PRINT 1 3",
    #         "PRINT 1 4"
    #     ]
    # ))


    # print(solution(
    #     [
    #         "UPDATE 1 1 a",
    #         "UPDATE 1 2 b",
    #         "UPDATE 2 1 c",
    #         "UPDATE 2 2 d",
    #         "MERGE 1 1 1 2",
    #         "MERGE 2 2 2 1",
    #         "MERGE 2 1 1 1",
    #         "PRINT 1 1",
    #         "UNMERGE 2 2",
    #         "PRINT 1 1"
    #     ]
    # ))

    print(solution(
        [
            "UPDATE 1 1 a",
            "UPDATE 1 2 b",
            "UPDATE 2 1 c",
            "UPDATE 2 2 d",
            "MERGE 1 1 1 2",
            "MERGE 2 2 2 1",
            "MERGE 2 1 1 1",
            "PRINT 1 1",
            "UNMERGE 2 2",
            "PRINT 1 1",
            "UPDATE 1 1 e",
            "MERGE 1 1 2 2",
            "PRINT 1 1",
            "PRINT 2 2"
        ]
    ))