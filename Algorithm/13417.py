# 백준 13417
# 카드 문자열

t = int(input())
for _ in range(t):
    make_cards = []
    n = int(input())
    cards = list(input().split())
    make_cards.append(cards[0])
    for i in range(n-1):
        if make_cards[0] >= cards[i+1]:
            make_cards.insert(0, cards[i+1])
        else:
            make_cards.append(cards[i+1])
    res = ''.join(make_cards)
    print(res)
