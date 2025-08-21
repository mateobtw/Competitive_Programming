n = int(input())
total = 0
minimum = 0
for _ in range(n):
    a, b = map(int, input().split())
    total -= a
    total += b
    # if total > minimum:
    #     minimum = total
    minimum = max(minimum, total)
print(minimum)
