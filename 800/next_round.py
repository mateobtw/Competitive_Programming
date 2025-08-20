n, k = map(int, input().split())
pun = list(map(int, input().split()))
corte = pun[k - 1]
print(sum(1 for i in pun if i >= corte and i > 0))
