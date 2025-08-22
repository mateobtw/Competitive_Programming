s, n = map(int, input().split())

data = []

for _ in range(n):
    x, y = map(int, input().split())
    data.append([x, y])

data.sort()

for a, b in data:
    if s > a:
        s += b
    else:
        print("NO")
        break
else:
    print("YES")
