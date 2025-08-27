# n, lo = map(int, input().split())
# posiciones = list(map(int, input().split()))
# posiciones.sort()

# minima = posiciones[0]
# for i in range(1, n):
#     distancia = posiciones[i] - posiciones[i - 1]
#     nose = distancia / 2
#     if nose > minima:
#         minima = nose

# xd = lo - posiciones[n - 1]
# if xd > minima:
#     minima = xd

# print(minima)

n, l = map(int, input().split())
a = list(map(int, input().split()))
a.sort()

inicio = a[0]
final = l - a[-1]

max_gap = 0
for i in range(1, n):
    gap = a[i] - a[i - 1]
    if gap > max_gap:
        max_gap = gap

d = max(inicio, final, max_gap / 2)
print(d)
