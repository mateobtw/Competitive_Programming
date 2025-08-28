n, m, a, b = map(int, input().split())

normal = n * a
combo = (n // m) * b + min((n % m) * a, b)
print(min(normal, combo))
