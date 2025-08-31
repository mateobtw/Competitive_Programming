n = list(map(int, input()))

m = len(n)
first = n[0]
if first >= 5 and first != 9:
    n[0] = 9 - first

for i in range(1, m):
    x = n[i]
    n[i] = min(x, 9 - x)

# for i in range(1, m):
#     x = n[i]
#     if x >= 5:
#         n[i] = 9 - x

print("".join(map(str, n)))
