import math

n, k = map(int, input().split())
impares = math.ceil(n / 2)  # ceil (n + 1) // 2
if k <= impares:
    print(2 * k - 1)
else:
    print(2 * (k - impares))
