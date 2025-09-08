n = int(input())

laptops = []
for _ in range(n):
    a, b = map(int, input().split())
    laptops.append((a, b))

# price = sorted(laptops)
# quality = sorted(laptops, key=lambda x: x[1])

# print("Poor Alex" if price == quality else "Happy Alex")

laptops.sort()
for i in range(1, n):
    if laptops[i - 1][1] > laptops[i][1]:
        print("Happy Alex")
        break
else:
    print("Poor Alex")
