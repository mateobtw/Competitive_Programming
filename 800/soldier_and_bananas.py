first_banana, dollars, bananas = map(int, input().split())
total = first_banana * ((bananas * (bananas + 1) / 2))
borrowed = int(total - dollars)
print(borrowed if borrowed > 0 else 0)
