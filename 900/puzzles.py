n, m = map(int, input().split())
p = list(map(int, input().split()))
p.sort(reverse=True)
x = float("inf")
for i in range(m - n + 1):
    x_new = p[i] - p[i + n - 1]
    x = min(x, x_new)
print(x)
