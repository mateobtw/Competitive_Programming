# n = int(input())

# d = [100, 20, 10, 5, 1]
# bills = 0
# i = 0
# while n != 0:
#     cur = d[i]
#     if n >= cur:
#         n -= cur
#         bills += 1
#     else:
#         i += 1
# print(bills)

n = int(input())

ans = 0
for d in (100, 20, 10, 5, 1):
    ans += n // d
    n %= d

print(ans)
