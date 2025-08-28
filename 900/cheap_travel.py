n, m, a, b = map(int, input().split())

cost = 0
if m >= n:
    cost = m
elif min(a, b / m) == a:
    cost = n * a
else:
    ent = n // m
    cost += ent * b
    res = n % m
    if res != 0:
        cost += min(res * a, res * b)
print(cost)
