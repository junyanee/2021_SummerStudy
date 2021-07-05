h, b, c, s = map(int, input().split())
space = h * b * c * s
volume = space / 8 / 1024 / 1024
print('%.1f' %volume, "MB")