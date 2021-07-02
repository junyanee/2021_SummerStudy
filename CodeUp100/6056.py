a, b = map(int, input().split())
print(bool(((not b) and a) or ((not a) and b)))