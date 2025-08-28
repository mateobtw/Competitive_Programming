import bisect

shops = int(input())
prices = list(map(int, input().split()))
prices.sort()

days = int(input())

for _ in range(days):
    coins = int(input())
    ans = bisect.bisect_right(prices, coins)
    print(ans)

# for _ in range(days):
#     coins = int(input())
#     if coins < prices[0]:
#         print(0)
#     elif coins >= prices[shops - 1]:
#         print(shops)
#     else:
#         i = 0
#         while i < shops and coins >= prices[i]:
#             i += 1
#         print(i)
