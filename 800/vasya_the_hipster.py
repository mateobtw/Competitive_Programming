nym = list(map(int, input().split()))
nym.sort()
h = nym[0]
nh = (nym[1] - h) // 2
print(h, nh)

a, b = map(int, input().split())
fashion = min(a, b)
same = abs(a - b) // 2
print(fashion, same)
