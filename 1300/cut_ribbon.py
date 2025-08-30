n, a, b, c = map(int, input().split())
le = list(a, b, c)
le.sort()

i = 0
while n > 0:
    x0 = le[i]
    if n // x0 != 0:
        n -= x0
