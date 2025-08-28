n = int(input())
h = list(map(int, input().split()))
m = min(h)
M = max(h)
# i = n - 1 - h[::-1].index(m)
x = h[::-1].index(m)
i = n - 1 - x
j = h.index(M)


total = x + j
print(total if i >= j else total - 1)
