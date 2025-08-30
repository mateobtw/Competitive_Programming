n, m = map(int, input().split())
prices = list(map(int, input().split()))
prices.sort()

earnings = 0
for i in range(m):
    if prices[i] > 0:
        break
    earnings += prices[i]
print(-earnings)
