n, m, a, b = map(int, input().split())

cost = 0
if min(a, b / m) == a:
    cost = n * a
else:
    ent = n // m
    cost += ent * b
    res = n % m
    if res != 0:

        cost += res * b
print(cost)
